import sys

def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:]!=".py":
            sys.exit("Not a python file")
        else:
            print(countline(sys.argv[1]))

def countline(file):
    try:
        count=0
        with open(file,"r") as f:
            for line in f:
                if not (line.lstrip().startswith("#") or line.strip()==""):
                    count +=1
            return count
    except FileNotFoundError:
        sys.exit("file does not exist")

if __name__=="__main__":
    main()
