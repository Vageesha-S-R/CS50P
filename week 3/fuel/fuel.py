def main():
    f=get_fraction("Fraction: ")
    if f<=1:
        print("E")
    elif f>=99:
        print("F")
    else:
        print(f"{f}%")

def get_fraction(f):
    while True:
        try:
            s=input(f)
            x,y=s.split("/")
            num1=int(x)
            num2=int(y)
            if num2>=num1:
                return round((num1/num2)*100)

        except (ValueError ,ZeroDivisionError ):
            pass


main()
