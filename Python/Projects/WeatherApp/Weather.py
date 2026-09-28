import requests
import tkinter as tk
from PIL import ImageTk, Image
import random
import os

API_KEY = "b155432dc7efa6fec38f66a561c58626"

# color
dark_blue = '#1a1035'
lighter_blue = '#56d0ff'
light_blue = '#3a9fd6'
purple = '#6b4fa0'

# GUI System
root = tk.Tk()
root.title('WeatherApp')
root.geometry('520x560')
root.configure(bg='#0b1d3a')

# Canvas for particles (as background)
canvas = tk.Canvas(root, bg='#0b1d3a', highlightthickness=0)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Title Label
tk.Label(root, text='⛅ Weather App', font=('Georgia', 22, 'bold'),
         bg='#0b1d3a', fg='#56d0ff').pack(pady=(22, 4))

tk.Label(root, text='─' * 44, bg='#0b1d3a', fg='#1a3560').pack()

# Weather Icons
icon_label = tk.Label(root, bg='#0b1d3a')
icon_label.pack(pady=8)

# City Input
tk.Label(root, text='Enter a city name:', font=('Georgia', 12),
         bg='#0b1d3a', fg='#a0c8f0').pack(pady=(6, 2))

city_entry = tk.Entry(root, font=('Courier', 13), width=24,
                      bg='#112244', fg='white', insertbackground='#56d0ff',
                      relief='flat', bd=8,
                      highlightthickness=1, highlightcolor='#56d0ff',
                      highlightbackground='#1a3560')
city_entry.pack()

# Particles
particles = []
current_weather = ''

# Particles Creation
def create_particles():
    width = canvas.winfo_width()
    if width <= 1:
        width = 520
    x = random.randint(0, width)
    if current_weather == 'snow':
        size = random.randint(2, 4)
        speed = random.randint(2, 4)
        color = 'white'
        drift = random.uniform(-1.5, 1.5)
    elif current_weather == 'rain':
        size = random.randint(1, 2)
        speed = random.randint(2, 8)
        color = '#4a9eff'
        drift = random.uniform(-2, 2)
    else:
        return
    particle = canvas.create_oval(x, 0, x + size, size, fill=color, outline='')
    particles.append({'id': particle, 'vx': drift, 'vy': speed})

# Particles dropping
def update_particles():
    to_remove = []
    if current_weather in ['snow', 'rain']:
        for p in particles:
            canvas.move(p['id'], p['vx'], p['vy'])
            coords = canvas.coords(p['id'])
            if coords[1] > canvas.winfo_height():
                to_remove.append(p)
        for p in to_remove:
            canvas.delete(p['id'])
            particles.remove(p)
        if random.random() < 0.3:
            create_particles()
    else:
        for p in particles:
            canvas.delete(p['id'])
        particles.clear()
    root.after(16, update_particles)

update_particles()

# Weather Function
def get_weather():
    global current_weather
    city = city_entry.get()
    if not city:
        result_label.config(text="Enter a city name.")
        icon_label.config(image='')
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if str(data.get('cod')) != '200':
            result_label.config(text="City Not Found", fg='#f87171')
            icon_label.config(image='')
        else:
            weather = data['weather'][0]['main']
            current_weather = weather.lower()

            temp_f = data['main']['temp']
            temp_c = round((temp_f - 32) * 5 / 9, 1)
            humidity = data['main']['humidity']

            result_label.config(
                text=f"Weather: {weather}\nTemperature: {temp_f} °F / {temp_c} °C\nHumidity: {humidity}%",
                bg='#0b1d3a',
                fg='white'
            )
            try:
                icon_file = None
                if weather.lower() == 'clear':
                    img = Image.open('Clear.jpg')
                elif weather.lower() == 'clouds':
                    img = Image.open('Clouds.jpg')
                elif weather.lower() == 'rain':
                    img = Image.open('Rain.jpg')
                elif weather.lower() == 'snow':
                    img = Image.open('snowflake.jpg')
                else:
                    icon_label.config(image='')
                    return
                if icon_file and os.path.exists(icon_file):
                    img = Image.open(icon_file).resize(50, 50)
                    photo = ImageTk.PhotoImage(img)
                    icon_label.config(image=photo)
                    icon_label.image = photo
                else:
                    icon_label.config(image='')
                    if icon_file:
                        print(f'Warning: {icon_file} not found!')

            except Exception as e:
                print(f'Error loading image: {e}')
                icon_label.config(image='')

    except requests.exceptions.RequestException as e:
        result_label.config(text='Connection Error. Check internet.')
        print(f'API Error: {e}')

# -- GUI Customization --
tk.Button(root, text='Get Weather', command=get_weather,
          background=lighter_blue, activebackground=light_blue,
          fg='#001122', font=('Georgia', 12, 'bold'),
          relief='flat', bd=0, padx=18, pady=7,
          cursor='hand2').pack(pady=14)

result_label = tk.Label(root, text="", wraplength=400,
                        bg='#0b1d3a', fg='white', font=('Courier', 12),
                        justify='left')
result_label.pack(pady=10)

city_entry.bind('<Return>', lambda e: get_weather())

root.mainloop()