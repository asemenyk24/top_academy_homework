import re

regex = re.compile(r'([0-1]\d|2[0-3]):[0-5]\d')
message = input("Enter your message: ")
if regex.search(message):
    print("Your message contains time:")
    print(regex.search(message))
else:
    print("Your message doesn't contain time or format incorrect!")
