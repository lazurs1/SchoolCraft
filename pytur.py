import turtle
import random

# Dictionary mapping shape names to their respective number of sides
shapes = {
    "Hypercube": 4,  # Simplified as a square for 2D representation
    "Pentagon": 5,
    "Hexagon": 6,
    "Heptagon": 7,
    "Octagon": 8,
    "Enneagon": 9,
    "Decagon": 10,
    "Hendecagon": 11,
    "Dodecagon": 12,
    "Tridecagon": 13,
    "Tetradecagon": 14
}

def setup_turtle():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Random Geometric Shapes in Multicolor")
    artist = turtle.Turtle()
    artist.speed(0)
    artist.hideturtle()
    return artist

def draw_shape(artist, num_sides, side_length):
    angle = 360 / num_sides
    artist.pendown()
    for _ in range(num_sides):
        artist.forward(side_length)
        artist.right(angle)
    artist.penup()

def main():
    artist = setup_turtle()
    
    while True:
        # Choose a random shape and its properties
        shape_name, num_sides = random.choice(list(shapes.items()))
        side_length = random.randint(20, 100)
        color = (random.random(), random.random(), random.random())
        
        # Set the pen color
        artist.pencolor(color)
        
        # Randomize starting position
        x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
        y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
        artist.penup()
        artist.goto(x, y)
        
        # Draw the selected shape
        draw_shape(artist, num_sides, side_length)

        # Optional: break after a certain number of shapes have been drawn
        # break

if __name__ == "__main__":
    main()
