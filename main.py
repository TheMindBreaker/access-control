import tkinter as tk
 
# creating window
window = tk.Tk()
 
# setting attribute
window.attributes('-fullscreen', True)
window.title("ACESS CONTROL V1.0.0")
 
# creating text label to display on window screen
label = tk.Label(window, text="Hello Tkinter!")
label.pack()
 
window.mainloop()