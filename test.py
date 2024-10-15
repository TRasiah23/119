import turtle as trtl
turtle= trtl.Turtle()
turtle.speed(3)
def shell():
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(100)  
    turtle.end_fill()

def draw_head():
    turtle.penup()
    turtle.goto(0, 100)  
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(30) 
    turtle.end_fill()

def draw_eyes():
    for x in [-15, 15]:  
        turtle.penup()
        turtle.goto(x, 130)  
        turtle.pendown()
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(10)  
        turtle.end_fill()
        
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(5)  
        turtle.end_fill()

def draw_legs():
    positions = [(70, 60), (70, -40), (-70, 60), (-70, -40)]  # Leg positions
    for pos in positions:
        turtle.penup()
        turtle.goto(pos)
        turtle.pendown()
        turtle.fillcolor("green")
        turtle.begin_fill()
        turtle.circle(20)  # Draw the leg
        turtle.end_fill()

# Function to draw the turtle's tail
def draw_tail():
    turtle.penup()
    turtle.goto(0, -100)  # Move to tail position
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.goto(-20, -130)  # Draw the tail
    turtle.goto(0, -100)  # Return to the base
    turtle.end_fill()

# Main function
def main():
    shell()  # Draw the shell
    draw_head()  # Draw the head
    draw_eyes()  # Draw the eyes
    draw_legs()  # Draw the legs
    draw_tail()  # Draw the tail

    turtle.done()  # Finish drawing

# Run the program
if __name__ == "__main__":
    main()
