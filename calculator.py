def add(*numbers):
    return sum(numbers)

def subtract(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero"
        result /= num
    return result

def get_numbers():
    try:
        raw_input = input("Enter numbers separated by space: ")
        number_list = list(map(float, raw_input.strip().split()))
        if len(number_list) < 2:
            print("Please enter at least two numbers.")
            return get_numbers()
        return number_list
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return get_numbers()

def calculator():
    while True:
        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Try again.")
            continue

        numbers = get_numbers()

        if choice == '1':
            print("Result:", add(*numbers))
        elif choice == '2':
            print("Result:", subtract(*numbers))
        elif choice == '3':
            print("Result:", multiply(*numbers))
        elif choice == '4':
            print("Result:", divide(*numbers))

if __name__ == "__main__":
    calculator()
