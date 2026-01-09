import time
from turtle import Screen
from player import Player
from boss import Enemy
from bullet import Bullet
from scoreboard import Scoreboard
import random

# ------------------ SETUP ------------------
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Shooter")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
enemies = []
bullets = []

# ------------------ CONTROLS ------------------
screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

def shoot():
    bullet = Bullet(player.position())
    bullets.append(bullet)

screen.onkey(shoot, "space")

# ------------------ SPAWN ENEMIES ------------------
def spawn_enemy():
    x = random.randint(-380, 380)
    y = random.randint(200, 300)
    enemy = Enemy((x, y))
    enemies.append(enemy)

# Initial enemies
for _ in range(5):
    spawn_enemy()

# ------------------ GAME LOOP ------------------
game_is_on = True
last_spawn_time = time.time()

while True:  # run forever, but stop moving objects on game over
    time.sleep(0.05)
    screen.update()

    if game_is_on:  # only update movements while game is running
        # Move bullets
        for bullet in bullets:
            bullet.move()

        # Remove bullets off-screen
        for bullet in bullets[:]:
            if bullet.ycor() > 300:
                bullet.hideturtle()
                bullets.remove(bullet)

        # Move enemies downward
        for enemy in enemies[:]:
            enemy.move()
            if enemy.ycor() < -250:
                enemy.hideturtle()
                enemies.remove(enemy)
                if scoreboard.decrease():
                    game_is_on = False  # stop all movements

        # Check bullet collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.distance(enemy) < 20:
                    bullet.hideturtle()
                    enemy.hideturtle()
                    if bullet in bullets:
                        bullets.remove(bullet)
                    if enemy in enemies:
                        enemies.remove(enemy)
                    scoreboard.increase()

        # Spawn new enemies every 3 seconds
        current_time = time.time()
        if current_time - last_spawn_time >= 3.0:
            spawn_enemy()
            spawn_enemy()
            last_spawn_time = current_time
