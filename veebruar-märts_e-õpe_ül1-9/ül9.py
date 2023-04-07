from tkinter import *
raam = Tk()
raam.title("Tühi tahvel")
tahvel = Canvas(raam, width=600)

tahvel.create_rectangle(50,70,100,100, width=2, outline="blue")
tahvel.create_text(50,50, text="Tere!")

tahvel.create_polygon(100,100,150,150,200,100, fill="red",outline="black")

tahvel.pack()
raam.mainloop()
