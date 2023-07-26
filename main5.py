def get_product_in_range(start, end):
    if start > end:
        start, end = end, start  # Поміняємо місцями межі діапазону

    product = 1
    for num in range(start, end + 1):
        product *= num

    return product

def main():
    a = int(input("Enter the first number of the range: "))
    b = int(input("Enter the second number of the range: "))

    result = get_product_in_range(a, b)
    print("The product of numbers in the range is:", result)

if __name__ == "__main__":
    main()

