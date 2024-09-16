import sys
import csv
from tabulate import tabulate

pizza=[]
if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1],"r") as file:
                reader=csv.DictReader(file)
                for row in reader:
                    pizza.append(row)
            print(tabulate(pizza,headers="keys",tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("file does not exist")


