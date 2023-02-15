import turtle

kilpkonna_juhised = []

f = open('kilpkonn.txt','r')
print(f.read())
for rida in f:
    kilpkonna_juhised.append(rida.strip)

def joonisa_kujund(kujund, kilpkonn):
    for käsk in kujund:
        if käsk[0] == "edasi":
            kilpkonn.forward(int(käsk[1]))
        elif käsk[0] == "tagasi":
            kilpkonn.backward(int(kä[1]))
        elif käsk[0] == "paremale":
            kilpkonn.right(int(käsk[1]))
        elif käsk[0] == "vasakule":
            kilpkonn.left(int(käsk[1]))

print(kilpkonna_juhised)

turtle.exitonclick()
