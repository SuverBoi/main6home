def draw_square(side_length, symbol, filled):
    if filled:
        for i in range(side_length):
            print(symbol * side_length)
    else:
        for i in range(side_length):
            if i == 0 or i == side_length - 1:
                print(symbol * side_length)
            else:
                print(symbol + " " * (side_length - 2) + symbol)

draw_square(5, "*", True)  # Заповнений квадрат
print()
draw_square(5, "*", False)  # Порожній квадрат
