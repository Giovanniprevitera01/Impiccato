import tkinter as tk
import sqlite3

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

def Database():
    global conn, cursor
    # Connect database
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    # Query create table
    cursor.execute("CREATE TABLE IF NOT EXISTS 'user' (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")



# Start menu
app.mainloop()