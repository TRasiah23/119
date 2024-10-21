import turtle as trtl

# Define function to draw a turtle
def draw_turtle(painter, x, y):
    painter.penup()
    painter.shape("turtle")
    painter.turtlesize(6)
    painter.goto(x, y)
    painter.color("green")
    painter.stamp()

# Draw a more realistic cat
def draw_cat(painter, x, y):
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    
    # Draw body
    painter.begin_fill()
    painter.circle(40)  # Main body
    painter.end_fill()

    # Draw head
    painter.goto(x, y + 60)
    painter.begin_fill()
    painter.circle(25)  # Head
    painter.end_fill()

    # Draw eyes
    painter.goto(x - 7, y + 90)
    painter.color("white")
    painter.begin_fill()
    painter.circle(5)  # Left eye
    painter.end_fill()

    painter.goto(x + 7, y + 90)
    painter.color("white")
    painter.begin_fill()
    painter.circle(5)  # Right eye
    painter.end_fill()

    # Draw pupils
    painter.goto(x - 7, y + 90)
    painter.color("black")
    painter.begin_fill()
    painter.circle(2)  # Left pupil
    painter.end_fill()

    painter.goto(x + 7, y + 90)
    painter.begin_fill()
    painter.circle(2)  # Right pupil
    painter.end_fill()

    # Draw ears
    painter.goto(x - 15, y + 45)
    painter.color("gray")
    painter.begin_fill()
    painter.goto(x - 10, y + 60)
    painter.goto(x, y + 45)
    painter.end_fill()

    painter.goto(x + 15, y + 45)
    painter.begin_fill()
    painter.goto(x + 10, y + 60)
    painter.goto(x, y + 45)
    painter.end_fill()

    # Draw whiskers
    painter.goto(x - 15, y + 30)
    painter.pendown()
    painter.goto(x + 15, y + 30)
    painter.penup()

    # Draw tail
    painter.goto(x - 30, y)
    painter.pendown()
    painter.goto(x - 40, y + 10)
    painter.goto(x - 30, y + 5)
    painter.penup()

def draw_bird(painter, x, y):
    painter.penup()
    painter.goto(x, y)
    painter.color("blue")
    
    # Draw body
    painter.begin_fill()
    painter.circle(15)  # Body
    painter.end_fill()

    # Draw head
    painter.goto(x, y + 20)
    painter.begin_fill()
    painter.circle(10)  # Head
    painter.end_fill()

    # Draw wings
    painter.goto(x - 15, y + 10)
    painter.pendown()
    painter.goto(x - 5, y)
    painter.goto(x, y + 10)
    painter.penup()

    # Draw beak
    painter.goto(x + 10, y + 20)
    painter.pendown()
    painter.goto(x + 15, y + 25)
    painter.goto(x + 10, y + 25)
    painter.penup()

def get_user_input():
    valid_animals = {"cats": draw_cat, "turtles": draw_turtle, "birds": draw_bird}
    
    while True:
        user_input = input("I draw animals. What animal and how many would you like me to draw? (e.g., 3 cats): ").strip().lower()
        parts = user_input.split()
        
        num = 1
        animal_type = None
        last_num = None
        
        for part in parts:
            if part.isdigit():
                last_num = int(part)
            elif part in valid_animals:
                animal_type = part
        
        if animal_type:
            num = last_num if last_num is not None else num
            num = min(num, 30)  

            if num > 0:
                return animal_type, num
            else:
                print("Invalid number. Please enter a valid number (1-30).")
        else:
            print("Invalid input. Please enter a valid animal type (cats, turtles, birds) and a valid number (1-30).")

animal_type, num = get_user_input()

screen = trtl.Screen()
screen.bgcolor("white")  # Set background color to white
painter = trtl.Turtle()
painter.speed(0)

# Starting coordinates and offset values
x_start, y_start = -200, 200
x_offset, y_offset = 100, -100
animal_func = {
    "turtles": draw_turtle,
    "cats": draw_cat,
    "birds": draw_bird
}

for i in range(num):
    position_x = x_start + i * x_offset
    position_y = y_start + i * y_offset
    animal_func[animal_type](painter, position_x, position_y)

painter.hideturtle()
screen.mainloop()
