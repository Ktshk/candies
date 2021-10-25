import turtle
import random
k=random.randint(10,26)
l=[]
x=0
turtle.Screen().setup(1500, 800)
turtle.Screen().addshape('pics/w.gif')
turtle.Screen().addshape('pics/r.gif')
turtle.Screen().addshape('pics/b.gif')
for i in range(-700,600,1300//k):
    if x==k:
        break
    t=turtle.Turtle()
    l.append(t)
    l[x].speed(0)
    l[x].penup()
    l[x].setpos(i,-43)
    l[x].shape('pics/w.gif')
    l[x].stamp()
    x=x+1
x=0
z=''
while k!=0:
    if x%2==0:
        a=int(turtle.Screen().numinput("красный", "введите 1 или 2",minval=1,maxval=2))
    else:
        a=int(turtle.Screen().numinput("синий", "введите 1 или 2",minval=1,maxval=2))
    if a>k:
        continue
    if x%2==0:
        for i in range(k-a,k):
            l[i].shape('pics/r.gif')
            l[i].stamp()
    else:
        for i in range(k-a,k):
            l[i].shape('pics/b.gif')
            l[i].stamp()
    k=k-a
    x=x+1
t=turtle.Turtle()
if x%2==0:
    t.write("красные проиграли",align='center', font=("Arial", 48, "bold"))
else:
    t.write("синие проиграли",align='center', font=("Arial", 48, "bold"))
turtle.Screen().mainloop()
