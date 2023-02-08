import turtle # impordib turtle'i

t = turtle.Turtle() #muutuja t

s = int(input("Sisesta ruudu külje pikkus: ")) #muutuja s, kasutaja sisestab ruudu küljepikkuse

for _ in range(4): # turtle'i liikumine
    t.forward(s) #turtle liigub otse
    t.left(90) #turtle keerab 90 kraadi vasakule