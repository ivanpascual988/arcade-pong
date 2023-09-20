"""
Programa que recrea el mitigo juego del arcade-pong gracias a la biblioteca turtle

@Author Ivan Pascual
"""

# Importamos los modulos
import time
import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("ARCADE PONG by Ivan Pascual")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)       # No se actualiza la ventana, a no ser que lo indiquemos

# Dibujo una línea en el medio del campo
linea = turtle.Turtle()
linea.speed(0)
linea.color("white")
linea.width(5)
linea.penup()
linea.goto(0, 300)
linea.pendown()
linea.goto(0, -300)
linea.hideturtle()

# Configuracion de los jugadores
nombre_J1 = ventana.textinput("J1", "Nombre del primer jugador:")
nombre_J2 = ventana.textinput("J2", "Nombre del segundo jugador:")
puntuacion_J1 = 0
puntuacion_J2 = 0
jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

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
pelota.dx = 0.250   # Velocidad en el eje x
pelota.dy = 0.250   # Velocidad en el eje y

# Funciones 
def mostrar_jugador1():
    """
    Funcion para mostrar el nombre del jugador1 y su puntuación
    """
    jugador1.hideturtle()   # escondemos la tortuga
    jugador1.penup()        # Elimina la linea desde el inicio
    jugador1.color("blue")
    jugador1.clear()        # Elimina el texto anterior
    jugador1_mas_puntuacion1 = nombre_J1.upper() + " - " + str(puntuacion_J1)
    jugador1.goto(-300,250)
    jugador1.write(jugador1_mas_puntuacion1, False, align="left", font=("Arial", 20, "normal"))

def mostrar_jugador2():
    """
    Funcion para mostrar el nombre del jugador2 y su puntuación
    """
    jugador2.hideturtle()   # escondemos la tortuga
    jugador2.penup()        # Elimina la linea desde el inicio
    jugador2.color("orange")
    jugador2.clear()        # Elimina el texto anterior
    jugador2_mas_puntuacion2 = nombre_J2.upper() + " - " + str(puntuacion_J2)
    jugador2.goto(300, 250)
    jugador2.write(jugador2_mas_puntuacion2, False, align="right", font=("Arial", 20, "normal"))

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

# Muestro a los jugadores
mostrar_jugador1()
mostrar_jugador2()

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
        pelota.setx(380)  
        pelota.dx *= -1     # cambio la direccion
        pelota.dx += 0.1    # aumento la velocidad

    # Colision con la paleta izquierda
    elif (pelota.dx < 0) and (-380 < pelota.xcor() < -370) and (paleta_izquierda.ycor() + 50 > pelota.ycor() > paleta_izquierda.ycor() - 50):
        pelota.color("blue")
        pelota.setx(-380)
        pelota.dx *= -1     # cambio la direccion
        pelota.dx += 0.1    # aumento la velocidad
    
    # Punto cuando la pelota sale de la pantalla
    if pelota.xcor() > 390:
        puntuacion_J1 += 1
        time.sleep(2)
        pelota.color("white")
        pelota.goto(0, 0)   # vuelve al inicio
        pelota.dx *= -1     # cambia de direccion
        mostrar_jugador1()  # Actualizo el jugador 1

    elif pelota.xcor() < -390:
        puntuacion_J2 += 1
        time.sleep(2)
        pelota.color("white")
        pelota.goto(0, 0)   # vuelve al inicio
        pelota.dx *= -1     # cambia de direccion
        mostrar_jugador2()  # Actualizco el jugador 2