#code stub
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #d = string
    #remove the leading dollar sign
    d = d.replace("$","")
    #convert to float
    dfloat = float(d)
    return dfloat


def percent_to_float(p):

    #remove the trailing percent sign
    p = p.replace("%","")
    #convert to float
    pfloat = float(p)
    #divide the value to scale to actual percentage values
    pfloat = pfloat / 100

    return pfloat

main()
