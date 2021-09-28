from tkinter import *
import pyshorteners

def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)


root = Tk()
root.title("Url shortner")
root.geometry("400x300")
root.resizable(False, False)
root.config(background="#41B3A3")

photo = PhotoImage(file = "url.png")
root.iconphoto(False, photo)



# Declare variables
url = StringVar()
shorturl = StringVar()
# Design labels
Label(root, text="URL Shortner", bg="#41B3A3",fg="#2C3E50", font="verdana 22 ").place(x=80, y=10)

# Accepting URL as a Input
Label(root, text="Enter URL Here ", bg="#2C3E50", fg="#EAECEE", font="verdana 10 bold"
            , padx=2, pady=2).place(x=7, y=100)
Entry(root, textvariable=url, font="verdana 12", width=30).place(x=7, y=120)

# Creating button to give a call for convert function
Button(root, text="Convert...", bg="#E27D60", fg="#000", font="verdana 12 "
        , command=convert, relief=GROOVE).place(x=7, y=180)

# Displaying shortened URL
Label(root, text="Shortened URL - Copy & Paste in browser", bg="#2C3E50", fg="#EAECEE"
            , font="verdana 10 bold", padx=2, pady=2).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=35, font="verdana 12").place(x=7, y=270)

root.mainloop()

#@sujaykummari
