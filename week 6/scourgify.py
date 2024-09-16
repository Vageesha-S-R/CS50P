import sys
import csv

def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:]!=".csv" and sys.argv[2][-4:]!=".csv":
            sys.exit("Not a CSV file")
        else:
            readwrite(sys.argv[1],sys.argv[2])


def readwrite(input,output):
    try:
        with open(input) as file:
            reader=csv.DictReader(file)
            with open(output, "w") as f:
                header=["first", "last", "house"]
                writer=csv.DictWriter(f,fieldnames=header)
                writer.writeheader()
                for row in reader:
                    last,first=row["name"].split(", ")
                    house=row["house"]
                    writer.writerow({"first": first, "last": last,"house": house})
    except FileNotFoundError:
        sys.exit(f"could not read {input}")


if __name__=="__main__":
    main()

