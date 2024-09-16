e=input("Expression").strip()

x,y,z=e.split(" ")

match y:
    case "+":
        s=float(x)+float(z)
        print(s)
    case "-":
        s=float(x)-float(z)
        print(s)
    case "*":
        s=float(x)*float(z)
        print(s)
    case "/":
        s=float(x)/float(z)
        print(s)
    case _:
        print("invalid expresssion")

