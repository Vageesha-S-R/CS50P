import sys
from PIL import Image,ImageOps
import os

l= [".jpg",".jpeg",".png"]
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else:
    root1,ext1=os.path.splitext(sys.argv[1])
    root2,ext2=os.path.splitext(sys.argv[2])
    if ext1.lower() not in l or ext2.lower() not in l:
        sys.exit("invalid input")
    elif ext1.lower() != ext2.lower():
        sys.exit("input and output have different extensions")
    else:
        try:
            shirt=Image.open("shirt.png")
            with Image.open(sys.argv[1]) as file:
                image=ImageOps.fit(file,shirt.size)
                image.paste(shirt,mask=shirt)
                image.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("file does not exist")
