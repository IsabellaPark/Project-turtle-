import turtle
b = turtle.Turtle()
shape = input("Choose a shape, triangle, square or circle: ")
if shape == "triangle": 
  def triangle(length, color):
    b.speed(1)
    b.color(color)
    b.forward(length)
    b.left(120)
    b.forward(length)
    b.left(120)
    b.forward(length)
  c = input("Choose a color, red blue or yellow: ")
  l = input("Choose a length for the triangle, 100 or 50: ")
  triangle(l, c)

elif shape == "square":
  def square(length, color):
    b.speed(1)
    b.color(color)
    b.forward(length)
    b.left(90)
    b.forward(length)
    b.left(90)
    b.forward(length)
    b.left(90)
    b.forward(length)
  c = input("Choose a color, purple, green, or orange: ")
  l = input("Choose a length for the square, 100 or 50: ")
  square(l, c)

else:
  def circle(length, color):
    b.speed(1)
    b.color(color)
    b.circle(length)
  c = input("Choose a color, navy, pink, or violet: ")
  l = input("Choose a length for the circle,  ")
  circle(l, c)
    
