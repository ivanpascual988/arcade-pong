"Programa que recrea el mitigo juego del arcade-pong gracias a la biblioteca turtle"

# Importamos los modulos
import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("ARCADE PONG by Ivan Pascual")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)       # No se actualiza la ventana, a no ser que lo indiquemos

# Configuracion de la paleta izquierda
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)   # Velocidad inicial 0
paleta_izquierda.shape("square")
paleta_izquierda.color("blue")
paleta_izquierda.shapesize(stretch_wid=5, stretch_len=1)
paleta_izquierda.penup()    # Elimina la linea desde el inicio
paleta_izquierda.goto(-380, 0)      # Posicion inicial

# Configuracion de la paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)     # Velocidad inicial 0
paleta_derecha.shape("square")
paleta_derecha.color("orange")
paleta_derecha.shapesize(stretch_wid=5, stretch_len=1)
paleta_derecha.penup()    # Elimina la linea desde el inicio
paleta_derecha.goto(380, 0)      # Posicion inicial

# Configuracion de la pelota
pelota = turtle.Turtle()
pelota.speed(10)    # Velocidad inicial 10
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.125   # Velocidad en el eje x
pelota.dy = 0.125   # Velocidad en el eje y

# Funciones para mover las paletas
def paleta_izquierda_arriba():
    """ 
    Funcion para mover la paleta izquierda hacia arriba
    """
    y = paleta_izquierda.ycor()      # Obtengo la cordenada de la paleta izquierda en el eje y
    # Si la paleta no ha llegado a la cordenada 250 del eje y, aumento 10
    if y < 250:
        y += 10
    paleta_izquierda.sety(y)    # Defino la nueva coordenada del eje y

def paleta_izquierda_abajo():
    """ 
    Funcion para mover la paleta izquierda hacia abajo
    """
    y = paleta_izquierda.ycor()     # Obtengo la cordenada de la paleta izquierda en el eje y
    # Si la paleta no ha llegado a la cordenada -250 del eje y, disminuyo 10
    if y > -250:
        y -= 10
    paleta_izquierda.sety(y)    # Defino la nueva coordenada del eje y

def paleta_derecha_arriba():
    """ 
    Funcion para mover la paleta derecha hacia arriba
    """
    y = paleta_derecha.ycor()      # Obtengo la cordenada de la paleta derecha en el eje y
    # Si la paleta no ha llegado a la cordenada 250 del eje y, aumento 10
    if y < 250:
        y += 10
    paleta_derecha.sety(y)    # Defino la nueva coordenada del eje y

def paleta_derecha_abajo():
    """ 
    Funcion para mover la paleta derecha hacia abajo
    """
    y = paleta_derecha.ycor()     # Obtengo la cordenada de la paleta derecha en el eje y
    # Si la paleta no ha llegado a la cordenada -250 del eje y, disminuyo 10
    if y > -250:
        y -= 10
    paleta_derecha.sety(y)    # Defino la nueva coordenada del eje y

# Configuracion para controlar las paletas
ventana.listen()
ventana.onkeypress(paleta_izquierda_arriba, "w")
ventana.onkeypress(paleta_izquierda_abajo, "s")
ventana.onkeypress(paleta_derecha_arriba, "Up")
ventana.onkeypress(paleta_derecha_abajo, "Down")

# Buecle infinito para que no termine el juego
while True:
    # Actualizamos la ventana
    ventana.update()

    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Colisiones con los bordes superiores e inferiores
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    # Colision con la paleta derecha
    if (pelota.dx > 0) and (380 > pelota.xcor() > 370) and (paleta_derecha.ycor() + 50 > pelota.ycor() > paleta_derecha.ycor() - 50):
        pelota.color("orange")    
        pelota.dx *= -1     # cambio la direccion

    # Colision con la paleta izquierda
    elif (pelota.dx < 0) and (-380 < pelota.xcor() < -370) and (paleta_izquierda.ycor() + 50 > pelota.ycor() > paleta_izquierda.ycor() - 50):
        pelota.color("blue")
        pelota.dx *= -1     # cambio la direccion
    
    # Punto cuando la pelota sale de la pantalla
    if pelota.xcor() > 390:
        pelota.color("white")
        pelota.goto(0, 0)   # vuelve al inicio
        pelota.dx *= -1     # cambia de direccion

    elif pelota.xcor() < -390:
        pelota.color("white")
        pelota.goto(0, 0)   # vuelve al inicio
        pelota.dx *= -1     # cambia de direccion