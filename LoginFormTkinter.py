import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login Page")
window.geometry('340x440')
window.configure(bg="#FFEC9E")

def login():
    username_str = "admin"
    password_str = "1234"
    if username_entry.get()==username_str and password_entry.get()==password_str:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid Login Credentials")

frame = tkinter.Frame(bg="#FFEC9E")

login_label = tkinter.Label(
    frame, text="Login", bg="#FFEC9E", fg="#ED9455", font=("Helvetica", 50, "bold")
)

username_label = tkinter.Label(
    frame, text="Username :", bg="#FFEC9E", fg="#ED9455", font=("Helvetica", 16)
)

username_entry = tkinter.Entry(
    frame, font=("Helvetica", 16), bg="#FFBB70", fg="#FFFBDA"
)

password_entry = tkinter.Entry(
    frame, font=("Helvetica", 16), bg="#FFBB70", fg="#FFFBDA", show="*"
)

password_label = tkinter.Label(
    frame, text="Password : ", bg="#FFEC9E", fg="#ED9455", font=("Helvetica", 16)
)

login_button = tkinter.Button(
    frame, text="Login", bg="#ED9455", fg="#FFFBDA", font=("Helvetica", 24), command=login
)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0, sticky="w")
username_entry.grid(row=2, column=0, pady=10)
password_label.grid(row=3, column=0, sticky="w")
password_entry.grid(row=4, column=0, pady=10)
login_button.grid(row=6, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()