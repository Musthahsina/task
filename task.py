def print_hexagon(rows, cols):
    for row in range(rows):
        for col in range(cols):
            print(" --- ", end=" ")
        print()  # Newline after each row of the top of hexagons

        for col in range(cols):
            print("/   \\", end=" ")
        print()  # Newline after each row of the upper diagonals of hexagons

        for col in range(cols):
            print("\\   /", end=" ")
        print()  # Newline after each row of the lower diagonals of hexagons

        for col in range(cols):
            print(" --- ", end=" ")
        print()  # Newline after each row of the bottom of hexagons

# Printing 4*7 hexagon pattern
print_hexagon(4, 7)
print_hexagon(3,5)