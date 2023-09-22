print("~~~~~~~~~~~~~~~~~~~CALCULATOR~~~~~~~~~~~~~~~~~~~~~~~")

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1/num2)
else:
    print("Please enter a valid number")