def main():
    s = input("What time is it?")
    n = convert(s)
    if(n >= 7 and n <= 8):
        print("breakfast time")
    elif(n>= 12 and n<=13):
        print("lunch time")
    elif(n>= 18 and n<= 19):
        print("dinner time")

def convert(time):
    #time is a string

    #create a list where there first value is the hours and the second is the number of minutes past the hours
    n = time.split(":")
    #calculate the number of minutes
    minutes = int(n[0]) * 60
    #add on the number of excess minutes
    minutes = minutes + int(n[1])
    #convert to decimal time
    decTime = minutes / 60

    return decTime


if __name__ == "__main__":
    main()
