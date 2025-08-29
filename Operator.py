a = input("Enter a number: ")
b = input("Enter another number: ")

try:
    a = int(a)
    b = int(b)
    result = a + b
    print(f"The sum of {a} and {b} is {result}.")
except ValueError:
    print("Please enter valid integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
print("Operation completed.")               