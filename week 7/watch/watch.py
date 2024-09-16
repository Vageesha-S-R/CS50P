import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(?:.)*></iframe>",s):
        if l:=re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)",s):
            return f"https://youtu.be/{l.group(1)}"


if __name__ == "__main__":
    main()
