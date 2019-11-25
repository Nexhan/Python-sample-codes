#swapping_two_varriables_by_taking_user_input

user_input = input("Please enter first number:")
user_input1 = input("Please enter the second number:")

temp = user_input
user_input = user_input1
user_input1 = temp

print(f"The swapped is variables {user_input1} to {user_input}")
print(f"The swapped is variables {user_input} to {user_input1}")