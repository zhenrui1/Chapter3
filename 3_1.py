

"""
Relational Operator 
<, <=, >, >=, !=, ==
Logical Operator
and, or, not, in, not in
"""

# true_or_false = "b" > "a"; #True
# true_or_false = "z" < "!"; #False
# true_or_false = "z" < "!" and "b" > "a" #False
# true_or_false = "z" < "!" or "b" > "a" #True

# true_or_false = [3, 5] < [3, 7]


# true_or_false = 3 in [3, 8]
# "c" < "abc"
# true_or_false = "c" < "good" + "d"


# true_or_false = not("z" > "!" or "b" > "a") #False

# print("true of false", true_or_false)

# list1 = [6, 4, -5, 3.5]
# print(list1)
# list1.sort()
# print(list1)

# list2 = ["ha", "hi", "B", "7"]
# print(list2)
# list2.sort()
# print(list2)

state = "CA"
states = ["MD", "VA", "WV", "DE"]

is_in_list = state in states

print(not(is_in_list) and "VA" in states)

