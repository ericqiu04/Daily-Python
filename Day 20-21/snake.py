import turtle as t
STARTING = [(20,0), (0,0), (-20,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING:
            self.add_segment(position)
    def add_segment(self, position):
        new_segment = t.Turtle()
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for s in range(len(self.segments) - 1,0 , -1):
            newx = self.segments[s-1].xcor()
            newy = self.segments[s-1].ycor()
            self.segments[s].goto(newx, newy)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
