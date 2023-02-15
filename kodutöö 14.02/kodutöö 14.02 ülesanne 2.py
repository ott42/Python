import turtle

kilpkonna_juhised = []

f = open('kilpkonn.txt','r')
print(f.read())
for rida in f:
    kilpkonna_juhised.append(rida.strip)

f.close()
print(kilpkonna_juhised)

turtle.exitonclick()


