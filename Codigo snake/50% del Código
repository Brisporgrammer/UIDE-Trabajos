#Este es el trabajo autónomo 2, para este trabajo utilice las librerias que vienen en python.
#En este caso utilice turtle como medio gráfico y random para generar la comida de forma aleatoria.
#Estas dos librerias son del estandar de python, es decir no es necesario agregarlas al visual studio code.

#Se importan las librerias necesarias.

import turtle, random

#Definimos la pantalla del juego.

WIDTH = 600 #Ancho de la pantalla px.
HEIGHT = 400 #Alto de la pantalla px.
STEP = 20 #Avance de la serpiente.
DELAY_MS = 100 #Cada cuanto se actualiza el juego.

#Aqui personalizamos la pantalla que nos da turtle.

screen = turtle.Screen() #Crea la ventana de turtle
screen.title("Snake") #Titulo de la ventana.
screen.setup(width=WIDTH, height=HEIGHT)  #Usamos las variables que establecimos.
screen.bgcolor("black") #Pone el color de fondo de la ventana.
screen.tracer(0) #Evita el parpadeo.

#Creamos la serpiente e iniciamos el puntaje.

snake = [(0, 0), (-STEP, 0), (-2 * STEP, 0)] #Creamos a la serpiente inicial.
direction = "Right" #Donde esta ubicada la serpiente,
next_direction = "Right" #A donde se va a dirigir la serpiente.
score = 0 #Establecemos el puntaje inical.
game_over = False #La partida empieza.

#Creamos los objetos como la serpiente, el alimento.
#El texto del puntaje y en caso de colisionar el texto de "Game Over"

body = turtle.Turtle() #Es el cuerpo de la serpiente
body.shape("square") #Establece varios cuadrados como su cuerpo.
body.color("green") #Establece el color del cuerpo de la serpiente.
body.penup() #Evita que deje restos.
body.hideturtle() #Oculta el cursor del cuerpo de la memoria.

head = turtle.Turtle() #Crea la cabeza de la serpiente.
head.shape("square")  #Definimos la forma de la cabeza.
head.color("dark green") #Cambiamos el color de la cabeza de la serpiente.
head.penup() 
head.hideturtle() 

food = turtle.Turtle() #Crea el cuerpo para representar el alimento.
food.shape("circle") #Establecemos que la forma de la comida debe ser un circulo.
food.color("red") #Establecemos el color del alimento.
food.penup()
food.shapesize(0.8, 0.8) #Reduce el tamaño del alimento.

score_text = turtle.Turtle() #Crea un objeto para el puntaje.
score_text.hideturtle() 
score_text.color("white")  #Establece el color blanco para el puntaje.
score_text.penup()

message_text = turtle.Turtle() #Crea un objeto para el "Game over"
message_text.hideturtle() 
message_text.color("white") #Establece el color blanco para el texto.
message_text.penup()

#Establecemos que el alimento aparezca de forma aleatoria mientras la serpiente colisione con estos.

def random_food_position(): #Función para ubicar una posición valida para la comida.
    while True: #Repite hasta encontrarun lugar valido.
        x = random.randrange(-WIDTH // 2 + STEP, WIDTH // 2 - STEP, STEP) #Calcula en el eje x hasta encontrar un espacio libre ahí.
        y = random.randrange(-HEIGHT // 2 + STEP, HEIGHT // 2 - STEP, STEP) #Calcula en el eje y hasta encontrar un espacio libre ahí.
        if (x, y) not in snake: #Idenifica que la serpiente no este ahí.
            return x, y #Da el espacio valido encontrado.
