from datetime import date
import sys
import operator
import inflect

p=inflect.engine()

def main():
    dob=input("Date of Birth: ")
    try:
        diff=operator.sub(date.today(),date.fromisoformat(dob))
        print(convert(diff.days))
    except:
        sys.exit("Invalid Date")

def convert(s):
    min=s*24*60
    return f"{p.number_to_words(min,andword="").capitalize()} minutes"

if __name__ == "__main__":
    main()
