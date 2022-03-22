

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

answer = eval(input("How many gallons does a ten-gallon hat hold? "))

if (.5 <= answer <= 1):
    print("Good, ", end="")
else:
    print("No, ", end="")
print("it holds about 3/4 of a gallon.")