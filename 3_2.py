

# grade = 90
# condition = grade >=90
# if not condition:
#     #execute when true 
#     print("Your grade is A")
# else:
#     #execute when False 
#     print("Your grade is not A")


# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# try: 
#     print("1", isinstance(num1, str))
#     print("2", isinstance(num2, str))
#     if isinstance(num1, str) or isinstance(num2, str):
#         print("Data type not allowd! Please specify a numeric value.")
#     else:
#         if num1 > num2:
#             largerVal = num1 
#         else: 
#             largerVal = num2 

#         print("The larger value is", str(largerVal))
# except:
#     print("Data not allowed")

# answer = eval(input("How many gallons does a ten-gallon hat hold? "))

# if (.5 <= answer <= 1):
#     print("Good, ", end="")
# else:
#     print("No, ", end="")
# print("it holds about 3/4 of a gallon.")



# Today class
# if Statements (2 of 3)
# first_num = eval(input("Enter first number: "))
# second_num = eval(input("Enter second number: "))
# third_num = eval(input("Enter third number: "))

# max = first_num

# if second_num > max: 
#     max = second_num
# if third_num > max:
#     max = third_num
# print("The largest of the three number is " + str(max) + ".")


#You can also use this method to find the largest number
# numbers = []
# first_num = eval(input("Enter first number: "))
# second_num = eval(input("Enter second number: "))
# third_num = eval(input("Enter third number: "))
# numbers.append(first_num)
# numbers.append(second_num)
# numbers.append(third_num)
# msg = "The largest of the three numbers is " + str(max(numbers)) + "."
# print(msg)

# Nested if-else Statements (3 of 5)
# color = input("Enter a color (BLUE or RED): ")
# mode = input("Enter a mode (STEADY or FLASHING): ")
# color = color.upper()
# mode = mode.upper()

# result = ""

# if color == "BLUE":
#     if mode == "STEADY":
#         result = "Clear View."
#     else:   # mode is FLASHING
#         result = "Clouds Due."
# else:    # color is RED
#     if mode == "STEADY":
#         result = "Rain Ahead."
#     else:   # mode is FLASHING
#         result = "Snow Ahead."
# print("The weather forecast is", result)


# Nested if-else Statements (4 OF 5)
# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     result = "Break even."
# else:
#     if costs < revenue:
#         profit = revenue - costs
#         result = "Profit is ${0:,.2f}.".format(profit)
#         profit = revenue - costs
#         result = "Profit is $(0:,.2f).".format(profit)
#     else:
#         loss = costs - revenue 
#         result = "Profit is ${0:,.2f}.".format(loss)
# print(result)


# Another way to do it (Refactor)
# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     print("Break even.")
# result = "is ${0:,.2f}".format(revenue - costs)
# if (revenue - costs) < 0:
#     print("Loss " + result)
# print("Profit " + result)


# The elif Clause (2 of 6)
# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))

# if num1 > num2:
#     print("The largest value is", str(num1) + ".")
# elif num2 > num1:
#         print("The largest value is", str(num2) + ".")
# else: 
#         print("The two values are equal.")


# Try The elif Clause (3 of 6) Example 7 for Practice (May be similar to Test 2)


# The elif Clause (5 of 6)
# gpa = eval(input("Enter your gpa: "))

# if gpa >= 3.9:
#     honors = "summa cum laude."
# elif gpa >= 3.6:
#     honors = "magna cum laude."
# elif gpa >= 3.3:
#     honors = "cum laude."
# else:
#     honors = "."

# print("You graduated" + honors)


# Input Validation with if-elif-else Statements (1 of 2)
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# if num1.isdigit() and num2.isdigit():
#     print("The sum is", str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.")
#     else:
#         print("The first entry was not a proper number.")
# else:
#     print("The second entry was not a proper number.")


# Another way to do it 
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# if num1.isdigit() and num2.isdigit():
#     print("The sum is", str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.")
#     print("The first entry was not a proper number.")
#     print("The second entry was not a proper number.")


# True and Flase
# if 0:
#     print("This will not run...")
# if 7:
#     print("This will run...")
# if []:
#     print("This will not run...")
# if [1, 2, 99]:
#     print("This will run...")
# if True:
#     print("This will run...")
# if False:
#     print("This will not run...")





