x1 = int(input("Enter a number between 1 and 9 for x1: "))
x2 = int(input("Enter a number between 1 and 9 for x2: "))

y1 = input("Enter a letter between A and H for y1: ").upper()
y2 = input("Enter a letter between A and H for y2: ").upper()

# Determine the color of square 1
if ((x1 % 2 == 0 and ord(y1) % 2 == 0) or (x1 % 2 == 1 and ord(y1) % 2 == 1)):
    square1_color = 'dark_square_color'
else:
    square1_color = 'light_square_color'

# Determine the color of square 2
if ((x2 % 2 == 0 and ord(y2) % 2 == 0) or (x2 % 2 == 1 and ord(y2) % 2 == 1)):
    square2_color = 'dark_square_color'
else:
    square2_color = 'light_square_color'

# Check if both squares have the same color
if square1_color == square2_color:
    print("YES")
else:
    print("NO")

