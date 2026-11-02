
# Fibonacci Series - Recursive and Non-Recursive

# Non-Recursive Method
def fibonacci_non_recursive(n):
    a = 0
    b = 1

    print("Non-Recursive Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# Recursive Method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Main Program
while True:
    print("\n1. Non-Recursive")
    print("2. Recursive")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of terms: "))
        if n > 0:
            fibonacci_non_recursive(n)
        else:
            print("Enter a positive number")

    elif choice == 2:
        n = int(input("Enter number of terms: "))
        if n > 0:
            print("Recursive Fibonacci Series:")
            for i in range(n):
                print(fibonacci_recursive(i), end=" ")
            print()
        else:
            print("Enter a positive number")

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
