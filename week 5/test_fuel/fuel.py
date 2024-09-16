def main():
    f=input("Fraction: ")
    per=convert(f)
    print(gauge(per))

def convert(f):
    x,y=f.split("/")
    if int(x)>int(y):
        raise ValueError
    elif int(y)==0:
        raise ZeroDivisionError
    
    return int(round((int(x)/int(y))*100))


def gauge(percentage):
    if percentage<=1:
        return("E")
    elif percentage>=99:
        return("F")
    else:
        return(f"{percentage}%")

if __name__=="__main__":
    main()
