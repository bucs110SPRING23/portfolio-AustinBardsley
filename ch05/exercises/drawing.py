def main():
    import turtle
    sides = int(input("Sides:"))
    length = int(input("length:"))
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    def draw_eq_shape(sides,length):
        for _ in range(sides):
            t.forward(length)
            t.left(360/sides)
    draw_eq_shape(sides,length)

main()

        