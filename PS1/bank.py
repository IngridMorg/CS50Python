greeting = input("Greeting: ")

if(greeting.startswith("Hello") or greeting.startswith("hello")):
    print("$0")
elif(greeting.startswith("H") or greeting.startswith("h")):
    print("$20")
else:
    print("$100")