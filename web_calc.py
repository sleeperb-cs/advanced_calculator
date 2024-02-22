import math

def calculator():
    print("Welcome to the Advanced Calculator!")
    print("Available operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Square root (sqrt)")
    print("6. Exponent (^)")
    
    choice = input("Enter the number corresponding to your choice: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(f"Result: {num1 / num2}")

    elif choice == '5':
        num = float(input("Enter the number: "))
        print(f"Result: {math.sqrt(num)}")

    elif choice == '6':
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        print(f"Result: {math.pow(base, exponent)}")

    else:
        print("Invalid choice.")
        
if __name__ == "__main__":
    calculator()