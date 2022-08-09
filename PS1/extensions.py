#lets try the match thing

str = input("File name: ")
#convert the string to lower case so that we can be case-insensitive
str = str.lower()
#gif 0
#jpg 1
#jpeg 1
#png 2
#pdf 3
#txt 4
#zip 5

answers = ["image/gif","image/jpeg", "image/png", "application/pdf", "text/plain", "application/zip"]
if(".gif" in str):
    print(answers[0])
elif(".jpg" in str or ".jpeg" in str):
    print(answers[1])
elif(".png" in str):
    print(answers[2])
elif(".pdf" in str):
    print(answers[3])
elif(".txt" in str):
    print(answers[4])
elif(".zip" in str):
    print(answers[5])
else:
    print("application/octet-stream")