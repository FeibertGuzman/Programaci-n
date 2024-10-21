import tkinter as tk
from tkinter import messagebox
import random

# Definiciones constantes
SIZE = 5
PLAYER = 'P'
TREASURE = 'T'
OBSTACLE = 'O'
ENEMY = 'E'
EMPTY = '.'

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Juego de Aventuras: El Tesoro Perdido")
        self.window.geometry("300x300")
        self.grid_frame = tk.Frame(self.window)
        self.grid_frame.pack()

        self.grid = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]
        self.player_pos = (SIZE // 2, SIZE // 2)  # Posición inicial del jugador
        self.obstacles = self.place_obstacles(3)  # 3 obstáculos
        self.enemies = self.place_enemies(2)      # 2 enemigos
        self.treasure_pos = self.place_treasure()  # Colocar tesoro después de obstáculos y enemigos

        self.labels = self.create_grid_labels()
        self.display_grid()

        self.window.bind("<KeyPress>", self.key_handler)
        self.window.after(1000, self.enemy_move)  # Iniciar movimiento de enemigos
        self.window.mainloop()

    def create_grid_labels(self):
        labels = []
        for i in range(SIZE):
            row_labels = []
            for j in range(SIZE):
                label = tk.Label(self.grid_frame, text='', width=4, height=2, borderwidth=1, relief="solid")
                label.grid(row=i, column=j)
                row_labels.append(label)
            labels.append(row_labels)
        return labels

    def place_treasure(self):
        while True:
            x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
            if (x, y) != self.player_pos and (x, y) not in self.obstacles and (x, y) not in self.enemies:
                self.grid[x][y] = TREASURE
                return (x, y)

    def place_obstacles(self, count):
        obstacles = []
        while len(obstacles) < count:
            x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
            if (x, y) != self.player_pos and (x, y) not in obstacles:
                self.grid[x][y] = OBSTACLE
                obstacles.append((x, y))
        return obstacles

    def place_enemies(self, count):
        enemies = []
        while len(enemies) < count:
            x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
            if (x, y) != self.player_pos and (x, y) not in enemies and (x, y) not in self.obstacles:
                self.grid[x][y] = ENEMY
                enemies.append((x, y))
        return enemies

    def display_grid(self):
        for i in range(SIZE):
            for j in range(SIZE):
                if (i, j) == self.player_pos:
                    self.labels[i][j].config(text=PLAYER, bg='lightblue')
                elif self.grid[i][j] == TREASURE:
                    self.labels[i][j].config(text='', bg='gold')
                elif self.grid[i][j] == OBSTACLE:
                    self.labels[i][j].config(text='', bg='gray')
                elif self.grid[i][j] == ENEMY:
                    self.labels[i][j].config(text='', bg='red')
                else:
                    self.labels[i][j].config(text='', bg='white')

    def move_player(self, dx, dy):
        x, y = self.player_pos
        new_pos = (x + dx, y + dy)

        # Verificar colisiones
        if 0 <= new_pos[0] < SIZE and 0 <= new_pos[1] < SIZE:
            if new_pos in self.obstacles:
                self.show_message("¡Has chocado con un obstáculo!\nGAME OVER")
                self.window.quit()
            elif new_pos in self.enemies:
                self.show_message("¡Has sido atrapado por un enemigo!\nGAME OVER")
                self.window.quit()
            else:
                self.player_pos = new_pos
                if self.player_pos == self.treasure_pos:
                    self.show_message("¡Felicidades! Has encontrado el tesoro.\nFin del juego.")
                    self.window.quit()
                self.display_grid()
        else:
            self.show_message("Movimiento fuera de los límites.")

    def key_handler(self, event):
        if event.keysym == 'Up':
            self.move_player(-1, 0)
        elif event.keysym == 'Down':
            self.move_player(1, 0)
        elif event.keysym == 'Left':
            self.move_player(0, -1)
        elif event.keysym == 'Right':
            self.move_player(0, 1)

    def enemy_move(self):
        for index, (x, y) in enumerate(self.enemies):
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # Movimiento aleatorio
            new_pos = (x + dx, y + dy)
            if 0 <= new_pos[0] < SIZE and 0 <= new_pos[1] < SIZE and new_pos not in self.obstacles:
                self.grid[x][y] = EMPTY  # Vaciar la posición antigua
                self.grid[new_pos[0]][new_pos[1]] = ENEMY  # Mover enemigo
                self.enemies[index] = new_pos  # Actualizar la posición del enemigo

        self.display_grid()

        if self.player_pos in self.enemies:
            self.show_message("¡Has sido atrapado por un enemigo!\nGAME OVER")
            self.window.quit()

        self.window.after(1000, self.enemy_move)  # Mover enemigos continuamente

    def show_message(self, message):
        messagebox.showinfo("Mensaje", message)

if __name__ == "__main__":
    Game()
