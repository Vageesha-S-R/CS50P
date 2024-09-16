l=["a","e","i","o","u","A","E","I","O","U"]

def main():
    s=input("Input: ")
    print("Output: ",shorten(s))

def shorten(word):
    s=[]
    for c in word:
        if c not in l:
            s.append(c)
    output="".join(s)
    return output

if __name__=="__main__":
    main()
