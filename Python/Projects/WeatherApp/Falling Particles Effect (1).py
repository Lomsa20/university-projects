import tkinter as tk 
import random

window = tk.Tk()
window.geometry('500x500')
canvas = tk.Canvas(window, bg = '#0b1d3a') # for drawing On window
canvas.pack(fill = 'both', expand = True)

particles = []
def create_particles():
    x = random.randint(0,500)
    size = random.randint(2, 4)
    speed = random.uniform(2,4) # returns float numbers in that range e.g. 2.32, 2.5, 5.23...
    
    particle  = canvas.create_oval(x, 0, x+size, size, fill = 'white', outline = '') 
    # x+size, size creates snow flakes width and height 
    particles.append({
        'id': particle,
        'vx': random.uniform(-1,1), # moves negative left positive right and 0 dont move 
        'vy': speed
        })
def update_particles():
    # FIX: Don't modify list while iterating
    to_remove = []
    for p in particles:
        canvas.move(p['id'],p['vx'],p['vy'])
        coords = canvas.coords(p['id'])
        
        if coords[1] > canvas.winfo_height(): # winfo_height is windows max height
        # we compare because if it is bigger than will not display and added to different list
            to_remove.append(p)
    for p in to_remove:
        canvas.delete(p['id'])
        particles.remove(p)
        
    # spawn new particles
    if random.random() < 0.3:
        create_particles()
        
    window.after(16, update_particles)
        
update_particles()
window.mainloop()