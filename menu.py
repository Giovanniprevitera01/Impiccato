import tkinter as tk

app = tk.Tk()
app.geometry('800x600')
app.title('Menu v0.1')

# Label
label = tk.Label(app, text='Test', font=('Arial', 20))
label.pack(side='top')

# Button 1
start_butt = tk.Button(app, text='Start', width=10, height=2)
start_butt.pack(side='right', padx=10, pady=10)
# Button 2
start2_butt = tk.Button(app, text='Start2', width=10, height=2)
start2_butt.pack(side='right', padx=10, pady=10)

# Start menu
app.mainloop()