

def faces(s):
    s = s.replace(":)","🙂")
    s = s.replace(":(", "🙁")
    return s



def main():
    str = input("")
    string = faces(str)
    print(string)

main()