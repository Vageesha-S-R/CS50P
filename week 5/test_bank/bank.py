def main():
    n=input("greeting: ")
    print(f"${value(n)}")

def value(greetings):
    greetings=greetings.lower().strip()
    if greetings.startswith("hello"):
        return(0)
    elif "h" in greetings[0]:
        return(20)
    else:
        return(100)

if __name__=="__main__":
    main()
