import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    make_square(dave)
    turtle.mainloop() #Evita que la ventana se cierre

def make_square(dave):
    length = int(input('Tamaño de cuadrado: ')) # Esta funcion sirve para que el programa se espere a dar un enter para ejecutarse
    for i in range(4):
        make_line_and_turn(dave, length) # Al Colocar el 100 vamos a "Hardcodear" un valor 


def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)


if __name__ == '__main__':
    main()