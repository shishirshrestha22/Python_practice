# THIS IS THE PROGRAM ABOUT FILE HANDLONG

with open ("data.txt","r") as file:
    text = file.read()

lines = text.split("\n")
words = text.split()
characters = len(text)

print(" No of lines =", len(lines))
print("No of Words =" ,len(words))
