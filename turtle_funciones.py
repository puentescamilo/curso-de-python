import turtle

def run():
    window = turtle.Screen()
    dave = turtle.Turtle()
    make_square(dave)

def make_square(dave):
    raw_input() # Esta funcion sirve para que el programa se espere a dar un enter para ejecutarse
    make_line_and_turn(dave, 100) # Al Colocar el 100 vamos a "Hardcodear" un valor 


def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)


if __name__ == '__main__':
    run()