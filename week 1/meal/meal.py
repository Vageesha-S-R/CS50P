def main():
    time=input("what time is it? ").strip()
    val=convert(time)

    if 7.0<=val<=8.0:
        print("breakfast time")
    elif 12<=val<=13:
        print("lunch time")
    elif 18<=val<=19:
        print("dinner time")


def convert(time):
    hours,minutes=time.split(":")
    num1=float(hours)
    num2=float(minutes)
    val=num1+(num2/60)
    return val


if __name__ == "__main__":
    main()

