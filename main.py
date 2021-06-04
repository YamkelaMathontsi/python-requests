from tkinter import *
from tkinter import messagebox
import requests

root = Tk()
root.title("Chuck Norris Jokes")
root.geometry("500x500")
root.config(bg="pink")

# cn_joke = Message(root, text=get_chucks_joke())


def jokes():
    try:

        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        print(data["value"])
        messagebox.showinfo("JOke", data["value"])
    except requests.exceptions.ConnectionError as x:
        messagebox.showerror("GET PROPER WIFI", "Please check Connection")


btn = Button(root, text="Click for a Chuck", command=jokes, borderwidth=10)
btn.place(x=170, y=150)


root.mainloop()
