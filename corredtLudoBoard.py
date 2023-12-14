import turtle
import time
turtle.speed("fastest")

b = turtle.Turtle()
window = turtle.Screen()

def draw_square(center, length, color = 'white'):
    # takes the coordinates of the center of a square and
    # draws the square, given the length and color
    b.up()
    #goTopleft
    b.goto(center[0]-length/2, center[1]+length/2)
    
    b.down()
    b.fillcolor(color)
    b.begin_fill()
    
    #gotoTopRight
    b.goto(center[0]+length/2, center[1]+length/2)
    #gotoBottomRight
    b.goto(center[0]+length/2, center[1]-length/2)
    #gotoBottomLeft
    b.goto(center[0]-length/2, center[1]-length/2)
    #gotoTopLeft
    b.goto(center[0]-length/2, center[1]+length/2)
    
    b.end_fill()

#if you want to see exactly how the board is created,
# comment out this turtle.tracer(0, 0) line. It makes the process instantaneous
turtle.tracer(0, 0)


#draw the inner main square
draw_square((0,0), 120)
#draw the outer main square
draw_square((0,0), 600)

#draw each small square
for x in [-40, 0, 40]:
    for y in [80, 120, 160, 200, 240,280]:
        draw_square((x,y), 40)
        draw_square((-y,x), 40)
        draw_square((y,x), 40)
        
        draw_square((x,-y), 40)
        
draw_square((-280,40), 40)
draw_square((-280,40), 40)

colored_squares = { "blue": [(0,80), (0,120), (0,160), (0,200),(0,240), (40,240)],
                    "red": [(0,-80), (0,-120), (0,-160), (0,-200), (0,-240), (-40,-240)],
                    "green": [(-240,40), (-240,0), (-200,0), (-160,0), (-120,0), (-80,0)],
                    "yellow": [(240,-40), (240,0), (200,0), (160,0), (120,0), (80,0)]
    }

draw_square((180,180), 240, color = 'blue')
draw_square((-180,-180), 240, color = 'red')
draw_square((-180,180), 240, color = 'green')
draw_square((180,-180), 240, color = 'yellow')

# define function to draw the respective colours on the small boxes
def draw_fill(slots, color):
 
    for slot in slots:
        draw_square(slot, 40, color)

blue_positions = {1: (40, 240), 2:(40,200), 3:(40,160), 4:(40,120), 5:(40,80),
                  6:(80,40),7:(120,40), 8:(160,40), 9:(200,40), 10:(240,40),
                  11:(280, 40), 12:(280, 0), 13:(280,-40), 14:(240,-40), 15:(200,-40),
                  16:(160,-40), 17:(120,-40), 18:(80,-40), 19:(40,-80), 20:(40,-120),
                  21:(40,-160), 22:(40,-200), 23:(40,-240), 24:(40,-280), 25:(0,-280),
                  26:(-40,-280), 27:(-40, -240), 28:(-40, -200), 29:(-40, -160),
                  30:(-40,-120), 31:(-40, -80), 32:(-80,-40), 33:(-120, -40),
                  34:(-160, -40), 35:(-200, -40), 36:(-240, -40), 37:(-280, -40),
                  38:(-280,0), 39:(-280, 40), 40:(-240, 40), 41:(-200, 40),
                  42:(-160, 40), 43:(-120, 40), 44:(-80, 40), 45:(-40,80),
                  46:(-40,120), 47:(-40,160), 48:(-40, 200),49:(-40, 240),
                  50:(-40, 280), 51:(0,280), 52:(0,240), 53:(0,200), 54:(0,160),
                  55:(0,120), 56:(0,80), 57:(0,40)}


red_positions = {}


for x in blue_positions:
    y = x-26
    z = x+26
    if y>0 and y<26:
        red_positions[y]= blue_positions[x]
    if z>26 and z<52:
        red_positions[z] = blue_positions[x]
#print(red_positions)

remaining_red_positions = [26,52,53,54,55,56,57]
remaining_red_coordinates = [(40,280), (0, -240), (0, -200), (0, -160),
                             (0, -120), (0, -80), (0, -40)]
for x in range(len(remaining_red_positions)):
    red_positions[remaining_red_positions[x]] = remaining_red_coordinates[x]

#print(red_positions)


# draw the colors on the respective boxes
for color in colored_squares:
    draw_fill(colored_squares[color], color)

'''
bluePiece = turtle.Turtle()

# Set the shape of the Turtle to "circle"
bluePiece.shape("circle")
bluePiece.color("blue")
bluePiece.penup()  # Lift the pen to move without drawing
#player1.goto(new_x, new_y)
bluePiece.goto(120,120)


redPiece = turtle.Turtle()

# Set the shape of the Turtle to "circle"
redPiece.shape("circle")
redPiece.color("red")
redPiece.penup()  # Lift the pen to move without drawing
#player1.goto(new_x, new_y)
redPiece.goto(-120,-120)
'''

class Piece:
    def __init__(self, color="black", position=(0, 0)):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(position)

    def set_color(self, color):
        self.turtle.color(color)

    def goto(self, position):
        time.sleep(0.8)
        self.turtle.goto(position[0], position[1])




'''
p = 1
while p<58:
    while (p > 51 and p<57):
        bluePiece.color("black")
        redPiece.color("black")
        break
    if p == 57:
        bluePiece.color("blue")
        redPiece.color("red")
    bluePiece.goto(blue_positions[p])
    time.sleep(1)
    window.update()
    redPiece.goto(red_positions[p])
    time.sleep(1)
    window.update()
    p+=1

'''


    
