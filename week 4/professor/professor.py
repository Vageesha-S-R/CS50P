import random

def main():
    level=get_level()
    score=0
    chance=3
    i=0
    while i<10:
        if chance==3:
            x=generate_integer(level)
            y=generate_integer(level)
        try:
            z=int(input(f"{x} + {y} ="))
            s=x+y
            if s==z:
                i+=1
                score+=1
                chance=3
                continue
            else:
                raise ValueError
        except (ValueError,NameError):
            print("EEE")
            chance-=1
            pass
        if chance==0:
            print(f"{x} + {y} ={s}",)
            chance=3
            i+=1
            continue
    print("score:",score)

def get_level():
    while True:
        try:
            n=int(input("Level: "))
            if 1<=n<=3:
                return n
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return(random.randint(0,9))
        case 2:
            return(random.randint(10,99))
        case 3:
            return(random.randint(100,999))




if __name__ == "__main__":
    main()
