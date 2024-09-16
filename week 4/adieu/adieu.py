import inflect
p=inflect.engine()
l=[]
while True:
    try:
        name=input("Name: ")
        l.append(name)

    except EOFError:
        print()
        print("Adieu, adieu, to",p.join(l))
        break
