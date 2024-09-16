import re

def main():
    print(count(input("Text: ")))


def count(s):
    l=re.findall(r"\bum\b",s,re.IGNORECASE)
    return len(l)




if __name__ == "__main__":
    main()
