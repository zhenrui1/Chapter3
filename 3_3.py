
# num = 0 #iterator / incrementor 
# while num < 10:
#     print("Hello World! " + str(num))
#     num += 1 # i = i + 1



# print("This program displays a famous movie quotations.")
# resps = ("1", "2", "3")
# resp = "0"

# while resp not in resps:
#     resp = input("Enter 1, 2 or 3: ")
#     if resp == "1":
#         print("Plastic.")
#     elif resp == "2":
#         print("Rosebud.")
#     elif resp == "3":
#         print("That's all folks.")


# count = 0 
# total = 0
# print("(Enter -1 to terminate program)")
# num = eval(input("Enter a nonnegative number: ")) #5
# min = num
# max = num
# while num != -1:
#     count += 1
#     total += num
#     if num < min:
#         min = num 
#     if num > max:
#         max = num 
#     num = num = eval(input("Enter a nonnegative number: ")) #5
# if count > 0:
#     print("Min: ", str(min))
#     print("Max ", str(max))
#     print("Average ", str(total / count))
# else:
#     print("No nonnegative numbers were entered")


#Refactor
# count = 0 
# numbers = 0
# print("(Enter -1 to terminate program)")
# num = eval(input("Enter a nonnegative number: ")) 
# numbers.append(num)
# while num != -1:
#     count += 1
#     num = num = eval(input("Enter a nonnegative number: ")) 
#     numbers.append(num)
# if count > 0:
#     print("Min: ", str(min(numbers)))
#     print("Max ", str(max(numbers)))
#     print("Average ", str(sum(numbers) / count))
# else:
#     print("No nonnegative numbers were entered")


# list1 = [300, 1, 2, 3, 60]
# list1.sort() # [1, 2, 3, 60, 300]
# list[0] # 1 - Lowest number in the list 
# list1[-1] # 300 - Largest number in the list


# Example 5
# i = 0 
# balance = eval(input("Enter initial deposit: "))
# rate = eval(input("Enter the annual rate of return: "))
# while balance < 1000000:
#     break 
#     balance += rate * balance #balance = balance * .04
#     i += 1
# print("In ", str(i), "years you will have a million dollars")


# Example 6
list1 = []
while True:
    num = eval(input("Enter a nonnnegative number: "))
    if num == -1:
        break 
    list1.append(num)

print(list1)