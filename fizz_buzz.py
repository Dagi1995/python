#if fizz it div by 3
#if buzz it div by 5
#if fizzbuzz it div by both 3 and 5


for add in range (1 , 100):
    if add % 3 == 0 and add % 5 == 0:
        print("fizzBuzz")
    elif add % 3 == 0:
        print("fizz")
    elif add % 5 == 0:
        print("buzz")
    
    else:
        print(add)

