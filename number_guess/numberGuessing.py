import random
a = 10
print(random.randint(a, 20))

def guess():
    b = random.randint(1, 10)
    print(b)
    ask = 0
    
    while ask != b:
        ask = int(input("Guess the number: "))
        if b < ask:
            print(f"Sorry {ask} is HIGH, try a Lower number: ")
            # return ask
        elif b > ask:
            print(f"Sorry {ask} is Low, try a Higher number")
    print(f"great! You Won!")
        
guess()