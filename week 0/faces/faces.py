def main():
    n=input()
    j=convert(n)
    print(j)

def convert(i):
    return i.replace(":)","🙂").replace(":(","🙁")

main()
