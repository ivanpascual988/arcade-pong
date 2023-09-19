"Programa que recrea el mitigo juego del arcade-pong gracias a la biblioteca turtle"

# Importamos los modulos
import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("ARCADE PONG by Ivan Pascual")
ventana.bgcolor("lightgreen")
ventana.setup(width=800, height=600)
ventana.tracer(0)       # No se actualiza la ventana, a no ser que lo indiquemos

# Configuracion de la paleta izquierda
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)   # Velocidad inicial 0
paleta_izquierda.shape("square")
paleta_izquierda.color("white")
paleta_izquierda.shapesize(stretch_wid=5, stretch_len=1)
paleta_izquierda.penup()    # Elimina la linea desde el inicio
paleta_izquierda.goto(-380, 0)      # Posicion inicial

# Configuracion de la paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("white")
paleta_derecha.shapesize(stretch_wid=5, stretch_len=1)
paleta_derecha.penup()    # Elimina la linea desde el inicio
paleta_derecha.goto(380, 0)      # Posicion inicial

# Configuracion de la pelota
pelota = turtle.Turtle()
pelota.speed(10)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 2   # Velocidadc en el eje x
pelota.dy = 2   # Velocidad en el eje y

while True:
    ventana.update()
