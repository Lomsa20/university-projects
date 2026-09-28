import os
import tempfile
import tkinter as tk
from tkinter import filedialog, messagebox

# 1. THIRD-PARTY LIBRARIES
# CustomTkinter for modern UI; Pillow & Pillow-HEIF for image handling; FPDF for generating PDFs.
import customtkinter as ctk
from fpdf import FPDF
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIF opener to support Apple iPhone .HEIC photos
register_heif_opener()

# Disable PIL's pixel limit so large photos don't throw decompression errors
Image.MAX_IMAGE_PIXELS = None

# Max width or height constraint before resizing images for PDF embedding
MAX_DIMENSION = 2000

# Set default application appearance mode and accent color
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class PDFConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Setup main window title and size
        self.title("PDF Converter Pro")
        self.geometry("550x650")
        self.resizable(False, False)  # Fixed size prevents layout glitches

        # List to store full file paths of uploaded images
        self.images = []

        # --- BUILD USER INTERFACE ---
        self.build_header()
        self.build_text_section()
        self.build_image_section()
        self.build_convert_button()

    # ------------------------------------------------------------------
    # UI BUILDING METHODS
    # ------------------------------------------------------------------

    def build_header(self):
        """Creates top title bar and the Light/Dark mode switch."""
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=(15, 5))

        title = ctk.CTkLabel(
            header_frame,
            text="📄 PDF Converter",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(side="left")

        # Switch to toggle between Light and Dark mode dynamically
        self.theme_switch = ctk.CTkSwitch(
            header_frame,
            text="Dark Mode",
            command=self.toggle_theme,
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.theme_switch.pack(side="right")
        self.theme_switch.select()  # Start in 'ON' state (Dark Mode)

    def build_text_section(self):
        """Creates section for multi-line document text input."""
        label = ctk.CTkLabel(
            self,
            text="1. Enter Document Text:",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        label.pack(anchor="w", padx=20, pady=(10, 2))

        self.text_box = ctk.CTkTextbox(self, height=120, font=ctk.CTkFont(size=12))
        self.text_box.pack(fill="x", padx=20, pady=(0, 10))

    def build_image_section(self):
        """Creates section for uploading, listing, and removing images."""
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.pack(fill="x", padx=20, pady=(5, 2))

        label = ctk.CTkLabel(
            top_frame,
            text="2. Attach Images:",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        label.pack(side="left")

        btn_upload = ctk.CTkButton(
            top_frame,
            text="+ Add Images",
            width=100,
            height=28,
            command=self.upload_images
        )
        btn_upload.pack(side="right")

        # Scrollable container to display attached image list
        self.image_list_frame = ctk.CTkScrollableFrame(self, height=140)
        self.image_list_frame.pack(fill="x", padx=20, pady=(0, 5))

        # Clear All Images button
        btn_clear = ctk.CTkButton(
            self,
            text="Clear All Images",
            fg_color="#ef4444",
            hover_color="#dc2626",
            height=26,
            command=self.clear_images
        )
        btn_clear.pack(anchor="e", padx=20, pady=(0, 10))

        # Show initial empty status message
        self.refresh_image_display()

    def build_convert_button(self):
        """Creates prominent bottom button to run the PDF conversion."""
        btn_convert = ctk.CTkButton(
            self,
            text="Convert to PDF",
            height=45,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.convert_to_pdf
        )
        btn_convert.pack(fill="x", padx=20, pady=(10, 20))

    # ------------------------------------------------------------------
    # EVENT HANDLERS & LOGIC
    # ------------------------------------------------------------------

    def toggle_theme(self):
        """Switches appearance mode between Dark and Light."""
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("Dark")
            self.theme_switch.configure(text="Dark Mode")
        else:
            ctk.set_appearance_mode("Light")
            self.theme_switch.configure(text="Light Mode")

    def upload_images(self):
        """Opens native file picker dialog to choose images."""
        file_paths = filedialog.askopenfilenames(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.heic")]
        )
        for path in file_paths:
            if path not in self.images:
                self.images.append(path)

        self.refresh_image_display()

    def remove_single_image(self, path):
        """Deletes a single selected image path from list."""
        if path in self.images:
            self.images.remove(path)
        self.refresh_image_display()

    def clear_images(self):
        """Empties the entire uploaded images list."""
        self.images.clear()
        self.refresh_image_display()

    def refresh_image_display(self):
        """Clears and re-renders items inside the scrollable list container."""
        # Remove old row widgets
        for widget in self.image_list_frame.winfo_children():
            widget.destroy()

        if not self.images:
            empty_lbl = ctk.CTkLabel(
                self.image_list_frame,
                text="No images attached yet.",
                text_color="gray"
            )
            empty_lbl.pack(pady=15)
            return

        # Render each path as an individual row item with a remove button
        for path in self.images:
            row = ctk.CTkFrame(self.image_list_frame, fg_color="transparent")
            row.pack(fill="x", pady=2)

            file_name = os.path.basename(path)
            lbl = ctk.CTkLabel(row, text=f"🖼️ {file_name}", anchor="w")
            lbl.pack(side="left", padx=5)

            btn_del = ctk.CTkButton(
                row,
                text="✕",
                width=24,
                height=24,
                fg_color="#fee2e2",
                hover_color="#fca5a5",
                text_color="#dc2626",
                command=lambda p=path: self.remove_single_image(p)
            )
            btn_del.pack(side="right", padx=5)

    def convert_to_pdf(self):
        """Executes full PDF conversion routine (Text formatting + Image embedding)."""
        text = self.text_box.get("1.0", "end").strip()

        # Input validation check
        if not text and not self.images:
            messagebox.showwarning("Warning", "Please add text or images first.")
            return

        # Save File Dialog
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not save_path:
            return  # User canceled save window

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)

        # 1. Write text input to PDF
        if text:
            for line in text.splitlines():
                # Encoding conversion prevents latin-1 PDF crashes on non-ASCII chars
                safe_line = line.encode("latin-1", "replace").decode("latin-1")
                pdf.cell(0, 8, txt=safe_line, ln=True)

        failed_images = []
        temp_files = []

        # 2. Process and embed images into PDF
        try:
            for image_path in self.images:
                try:
                    img = Image.open(image_path).convert("RGB")

                    # Downscale oversized images before saving temporary compressed copy
                    if img.width > MAX_DIMENSION or img.height > MAX_DIMENSION:
                        img.thumbnail((MAX_DIMENSION, MAX_DIMENSION), Image.LANCZOS)

                    # Create temporary JPG for PDF inserting
                    fd, temp_path = tempfile.mkstemp(suffix=".jpg")
                    os.close(fd)
                    img.save(temp_path, quality=85)
                    temp_files.append(temp_path)

                    pdf.ln(5)
                    pdf.image(temp_path, x=10, w=180)

                except Exception as err:
                    failed_images.append(f"{os.path.basename(image_path)}: {err}")

            # Save finished PDF file to disk
            pdf.output(save_path)

        finally:
            # Always remove temporary resized files after compilation
            for temp in temp_files:
                if os.path.exists(temp):
                    os.remove(temp)

        # Output result popups
        if failed_images:
            messagebox.showwarning(
                "Notice",
                "PDF saved, but skipped these failed images:\n\n" + "\n".join(failed_images)
            )
        else:
            messagebox.showinfo("Success", f"PDF successfully created:\n{save_path}")


# Entry point
if __name__ == "__main__":
    app = PDFConverterApp()
    app.mainloop()