n=input("greeting: ").lower().strip()

if "hello" in n:
    print("$0")
elif "h" in n[0]:
    print("$20")
else:
    print("$100")
