import random

def main():
    n=getinput("Level: ")
    l=random.randint(1,n)
    while True:
        g=getinput("Guess: ")
        try:
            if g<l:
                print("Too small!")
            elif g>l:
                print("Too large!")
            else:
                print("Just right!")
                raise EOFError
        except EOFError:
            break

def getinput(s):
    while True:
        try:
            x=int(input(s))
            if x<=0:
                raise ValueError
            else:
                return x
        except ValueError:
            pass



main()
