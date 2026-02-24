#Este es el trabajo autónomo 2, para este trabajo utilice las librerias que vienen en python.
#En este caso utilice turtle como medio gráfico y random para generar la comida de forma aleatoria.
#Estas dos librerias son del estandar de python, es decir no es necesario agregarlas al visual studio code.

#Se importan las librerias necesarias.

import turtle, random

#Definimos la pantalla del juego.

WIDTH = 600 
HEIGHT = 400 
STEP = 20 
DELAY_MS = 100 

#Aqui personalizamos la pantalla que nos da turtle.

screen = turtle.Screen() 
screen.title("Snake") 
screen.setup(width=WIDTH, height=HEIGHT) 
screen.bgcolor("black") 
screen.tracer(0) 

#Creamos la serpiente e iniciamos el puntaje.

snake = [(0, 0), (-STEP, 0), (-2 * STEP, 0)] 
direction = "Right" 
next_direction = "Right" 
score = 0
game_over = False

#Creamos los objetos como la serpiente, el alimento.
#El texto del puntaje y en caso de colisionar el texto de "Game Over"

body = turtle.Turtle()
body.shape("square") 
body.color("green") 
body.penup()
body.hideturtle() 

head = turtle.Turtle()
head.shape("square")  
head.color("dark green") 
head.penup() 
head.hideturtle() 

food = turtle.Turtle()
food.shape("circle") 
food.color("red") 
food.penup()
food.shapesize(0.8, 0.8) 

score_text = turtle.Turtle()
score_text.hideturtle() 
score_text.color("white")  
score_text.penup()

message_text = turtle.Turtle() 
message_text.hideturtle() 
message_text.color("white") 
message_text.penup()

#Establecemos que el alimento aparezca de forma aleatoria mientras la serpiente colisione con estos.

def random_food_position():
    while True: 
        x = random.randrange(-WIDTH // 2 + STEP, WIDTH // 2 - STEP, STEP) 
        y = random.randrange(-HEIGHT // 2 + STEP, HEIGHT // 2 - STEP, STEP)
        if (x, y) not in snake:
            return x, y 

#Funcion para variar el puntaje.

def update_score(): 
    score_text.clear() 
    score_text.goto(-WIDTH // 2 + 10, HEIGHT // 2 - 35) 
    score_text.write(f"Puntaje: {score}", font=("Consolas", 14, "normal")) 

#Funcion para redibujar la serpiente.

def draw_snake(): 
    body.clearstamps()  
    head.clearstamps()  
 
    hx, hy = snake[0]  
    head.goto(hx, hy)  
    head.stamp() 

    for x, y in snake[1:]:  
        body.goto(x, y) 
        body.stamp() 

#Combierte las instrucciones de dirreción encambio de cordenadas.

def direction_delta(name):
    if name == "Up":  
        return 0, STEP 
    if name == "Down":  
        return 0, -STEP  
    if name == "Left": 
        return -STEP, 0 
    return STEP, 0  

#Prohibe deplasarce en una dirección opuesta a la actual.

def is_opposite(a, b): 
    opposite = { 
        "Up": "Down",  
        "Down": "Up",
        "Left": "Right",  
        "Right": "Left", 
    } 
    return opposite[a] == b  

#Valida que la nueva dirección sea correcta y la guarda como verdadera.

def set_next_direction(new_dir): 
    global next_direction  
    if not is_opposite(direction, new_dir): 
        next_direction = new_dir  

#Las tres funciones que acabamos de ver, van de la mano, ya que son necesarias para el desplazamiento de la serpiente.

#Funcion para mostrar el mensaje de "Game Over" en caso de colisionar.

def show_game_over(): 
    message_text.clear()
    message_text.goto(0, 0)
    message_text.write( 
        "Game Over - presiona R para reiniciar",  
        align="center",  
        font=("Consolas", 16, "bold"),  
    )

#Funcion para reiniciar el juego, restablece todos los valores a su estado inicial y comienza el juego de nuevo.

def reset_game(): 
    global snake, direction, next_direction, score, game_over  

    snake = [(0, 0), (-STEP, 0), (-2 * STEP, 0)]  
    direction = "Right"  
    next_direction = "Right"  
    score = 0  
    game_over = False  

    message_text.clear() 
    food.goto(random_food_position()) 
    update_score() 
    draw_snake()  
    screen.update()  
    game_loop()  

#Funcion principal, encargada del movimiento de la serpiente, generar alimento detectar colisiones y actualizar la pantalla.

def game_loop(): 
    global direction, score, game_over  

    if game_over:  
        return  

    direction = next_direction 
    dx, dy = direction_delta(direction)  
    hx, hy = snake[0]  
    new_head = (hx + dx, hy + dy)  

    hit_wall = (  
        new_head[0] <= -WIDTH // 2  
        or new_head[0] >= WIDTH // 2  
        or new_head[1] <= -HEIGHT // 2  
        or new_head[1] >= HEIGHT // 2  
    ) 

    if hit_wall or new_head in snake:  
        game_over = True  
        show_game_over()  
        screen.update() 
        return  

    snake.insert(0, new_head)  

    if new_head == (int(food.xcor()), int(food.ycor())): 
        score += 1  
        food.goto(random_food_position())  
    else:  
        snake.pop()  

    update_score()  
    draw_snake()  
    screen.update()  
    screen.ontimer(game_loop, DELAY_MS) 

#Establece que teclas se utilizaran para el desplazamiento de la serpiente y para reiniciar el juego.

screen.listen() 
screen.onkey(lambda: set_next_direction("Up"), "Up") 
screen.onkey(lambda: set_next_direction("Down"), "Down") 
screen.onkey(lambda: set_next_direction("Left"), "Left") 
screen.onkey(lambda: set_next_direction("Right"), "Right") 
screen.onkey(reset_game, "r") 
screen.onkey(reset_game, "R") 

#Coloca la comida inicial, dibuja la serpiente inicial y empieza el juego.

food.goto(random_food_position()) 
update_score()  
draw_snake() 
game_loop() 
screen.mainloop() 