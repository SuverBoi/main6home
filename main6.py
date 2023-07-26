def count_number_function(start, end):
    count = 0
    for num in range(start, end):
        count += 1
    return count


def main():
    a = int(input("Choose the random number to count it (MAX 1 million):  "))
    count_range = count_number_function(1, 11)
    if a in range(0, 10):
         print("1")
    elif a in range(10, 100):
        print("2")
    elif a in range(100, 1000):
        print("3")
    elif a in range(1000, 10000):
        print("4")
    elif a in range(10000, 100000):
        print("5")
    elif a in range(100000, 1000000):
        print("6")
    elif a > 1000000:
        print("Error: Too big number")
    else:
        print("Error: Invalid input")

if __name__ == "__main__":
    main()
