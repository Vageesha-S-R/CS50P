from pyfiglet import Figlet
import sys
import random

figlet=Figlet()
l=["-f","--font"]
def main():
    if len(sys.argv)<2:
        f=random.choice(figlet.getFonts())
        fig(f)

    elif len(sys.argv)>2 and sys.argv[1] in l and sys.argv[2] in figlet.getFonts():
        f=sys.argv[2]
        fig(f)

    else:
        sys.exit("Invalid usage")

def fig(f):
    figlet.setFont(font=f)
    s=input("Input: ")
    print(figlet.renderText(s))

main()
