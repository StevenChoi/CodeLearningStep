# turtle 绘制奥运五环
# turtle 文档 https://docs.python.org/zh-cn/3/library/turtle.html
# 可使用函数+循环的形式
import turtle
t = turtle.Pen()

t.width(10)

#t.penup()
#t.goto(0, 0)
#t.pendown()
t.color('blue')
t.circle(50)

t.penup()
t.goto(120, 0)
t.pendown()
t.color('black')
t.circle(50)

t.penup()
t.goto(240, 0)
t.pendown()
t.color('red')
t.circle(50)

t.penup()
t.goto(60, -50)
t.pendown()
t.color('yellow')
t.circle(50)

t.penup()
t.goto(180, -50)
t.pendown()
t.color('green')
t.circle(50)


