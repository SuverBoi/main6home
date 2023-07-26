def find_min_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    d = int(input("Enter the fourth number: "))
    e = int(input("Enter the fifth number: "))

    min_number = find_min_of_five(a, b, c, d, e)
    print("The minimum number is:", min_number)

if __name__ == "__main__":
    main()
