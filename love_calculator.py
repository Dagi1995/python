name_my =input("Enter your name : ").lower()
name_you = input("Enter your partner name : ").lower()

name_1 = name_my + name_you

t = name_1.count("t")
r = name_1.count("r")
u = name_1.count("u")
e = name_1.count("e")

result_1 = t + r + u + e

name_2 = name_my + name_you

l = name_2.count("l")
o = name_2.count("o")
v = name_2.count("v")
e = name_2.count("e")

result_2 = l + o + v + e
result = str(result_1) + str(result_2)
result_as_int = int(result)

if result_as_int < 10 or  result_as_int > 90 :
    print(f"your score is {result_as_int} , you go together like coke and mentos")
elif result_as_int < 50 or  result_as_int > 40 : 
    print(f"your score is {result_as_int} , you are alright together")
else:
    print(f"your score is {result_as_int}.")