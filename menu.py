import tkinter as tk

app = tk.Tk()
app.geometry('800x600')
app.title('Menu v0.1')

label = tk.Label(app, text='Test')
label.pack(side='top')

start_butt = tk.Button(app, text='Start', width=10, height=2)
start_butt.pack(side='right', padx=10, pady=10)

start2_butt = tk.Button(app, text='Start2', width=10, height=2)
start2_butt.pack(side='right', padx=10, pady=10)

app.mainloop()