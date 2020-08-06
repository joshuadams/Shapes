import turtle
shape = turtle.Turtle()

# Parameter

# Square
def createSquare(size, col):
  shape.color(col)
  for i in range(4):
    shape.forward(size)
    shape.right(90)

# Triangle
def createTriangle(size, col):
  shape.color(col)
  for i in range(3):
    shape.forward(size)
    shape.right(120)

# Circle
def createCircle(size, col):
  shape.color(col)
  shape.circle(size)

shapes = {
  'circle' : createCircle,
  'triangle' : createTriangle,
  'square' : createSquare
}
playOn = 'Y'

while playOn == 'Y':
  # Specify the size, fillcolor, and change location
  shap = input('What do you want us to draw? ')
  col = input('What color would you want? ') 
  size = input('What size would you want? ')


  shapes[shap](size, col)
  playOn = input('Do you want to play again? (Y/N) ')