str = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
str = str.lower()
if("forty two" in str):
    print("Yes")
elif("forty-two" in str):
    print("Yes")
elif("42" in str):
    print("Yes")
else:
    print("No")
