from turtle import Turtle, Screen

wn = Screen()

def tree(length,t):
    if length > 5:
        t.forward(length) 
        t.right(40)       
        tree(length-15,t)
        t.left(80)        
        tree(length-15,t) 
        t.right(40)       
        t.backward(length)


t = Turtle()
t.left(90) 
t.speed(0) 

tree(100,t)

wn.exitonclick()
