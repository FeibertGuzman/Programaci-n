import tkinter as tk
import random

# Tamaño del tablero
WIDTH = 500
HEIGHT = 500
SEGMENT_SIZE = 20

# Clase para la serpiente
class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.segments = [(100, 100), (80, 100), (60, 100)]
        self.squares = []
        self.direction = 'Right'
        self.create_snake()

    def create_snake(self):
        for x, y in self.segments:
            square = self.canvas.create_rectangle(x, y, x + SEGMENT_SIZE, y + SEGMENT_SIZE, fill="green")
            self.squares.append(square)

    def move(self):
        head_x, head_y = self.segments[0]

        if self.direction == 'Right':
            new_head = (head_x + SEGMENT_SIZE, head_y)
        elif self.direction == 'Left':
            new_head = (head_x - SEGMENT_SIZE, head_y)
        elif self.direction == 'Up':
            new_head = (head_x, head_y - SEGMENT_SIZE)
        elif self.direction == 'Down':
            new_head = (head_x, head_y + SEGMENT_SIZE)

        self.segments = [new_head] + self.segments[:-1]

        for i, (x, y) in enumerate(self.segments):
            self.canvas.coords(self.squares[i], x, y, x + SEGMENT_SIZE, y + SEGMENT_SIZE)

    def change_direction(self, new_direction):
        opposites = {'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def grow(self):
        self.segments.append(self.segments[-1])
        square = self.canvas.create_rectangle(0, 0, SEGMENT_SIZE, SEGMENT_SIZE, fill="green")
        self.squares.append(square)

    def check_collision(self):
        head_x, head_y = self.segments[0]

        # Colisión con las paredes
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True

        # Colisión con sí misma
        if (head_x, head_y) in self.segments[1:]:
            return True

        return False

# Clase para la comida
class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.position = self.random_position()
        self.square = self.canvas.create_rectangle(self.position[0], self.position[1],
                                                   self.position[0] + SEGMENT_SIZE,
                                                   self.position[1] + SEGMENT_SIZE, fill="red")

    def random_position(self):
        x = random.randint(0, (WIDTH // SEGMENT_SIZE) - 1) * SEGMENT_SIZE
        y = random.randint(0, (HEIGHT // SEGMENT_SIZE) - 1) * SEGMENT_SIZE
        return x, y

    def respawn(self):
        self.canvas.coords(self.square, -SEGMENT_SIZE, -SEGMENT_SIZE, 0, 0)
        self.position = self.random_position()
        self.canvas.coords(self.square, self.position[0], self.position[1],
                           self.position[0] + SEGMENT_SIZE, self.position[1] + SEGMENT_SIZE)

# Funciones principales
def game_over():
    canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over", font=('Arial', 30), fill='red')
    root.after_cancel(game_loop)

def update():
    snake.move()

    # Si la serpiente choca, se acaba el juego
    if snake.check_collision():
        game_over()
        return

    # Si la serpiente come la comida
    if snake.segments[0] == food.position:
        snake.grow()
        food.respawn()

    root.after(100, update)

def change_direction(event):
    directions = {'Up': 'Up', 'Down': 'Down', 'Left': 'Left', 'Right': 'Right'}
    if event.keysym in directions:
        snake.change_direction(directions[event.keysym])

# Configuración del juego
root = tk.Tk()
root.title("Juego de la Culebrita")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = Snake(canvas)
food = Food(canvas)

root.bind("<KeyPress>", change_direction)

# Iniciar el bucle de juego
game_loop = root.after(100, update)

root.mainloop()
