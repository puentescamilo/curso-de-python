import turtle

def run():
    window = turtle.Screen()
    dave = turtle.Turtle()
    make_square(dave)

def make_square(dave):
    length = int(raw_input('Tamaño de cuadrado')) # Esta funcion sirve para que el programa se espere a dar un enter para ejecutarse
    make_line_and_turn(dave, length) # Al Colocar el 100 vamos a "Hardcodear" un valor 


def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)


if __name__ == '__main__':
    run()