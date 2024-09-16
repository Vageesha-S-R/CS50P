import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time:=re.search(r"^(([0-9][0-2]?):?([0-5][0-9])?) (AM|PM) to (([0-9][0-2]?):?([0-5][0-9])?) (AM|PM)$",s):
        num=time.groups()
        if int(num[1])>12 or int(num[5])>12:
            raise ValueError
        from_time=time_format(num[1],num[2],num[3])
        to_time=time_format(num[5],num[6],num[7])
        return f"{from_time} to {to_time}"

    else:
        raise ValueError

def time_format(hr,min,m):
    if m=="PM":
        if int(hr)==12:
            new_hr=12
        else:
            new_hr=int(hr)+12
    else:
        if int(hr)==12:
            new_hr=0
        else:
            new_hr=int(hr)
    if min==None:
        new_min=":00"
        new_time=f"{new_hr:02}"+new_min
    else:
        new_time=f"{new_hr:02}"+":"+min

    return new_time


if __name__ == "__main__":
    main()
