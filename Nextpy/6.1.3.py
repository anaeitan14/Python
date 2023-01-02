import tkinter as tk


window = tk.Tk()

def show():
    birthday_reveal = tk.Label(text="19/05/2000")
    birthday_reveal.pack()

birthday = tk.Label(window,text="Whats my birthday?", width=50, height=5,fg="red")
button = tk.Button(window, text="Click to find out!", width=15,height=5,command=show)

birthday.pack()
button.pack()


window.mainloop()

