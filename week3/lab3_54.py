#PROGRAM THAT ACCEPTS INTEGER INPUTS AS LONG AS THE WORD "STOP" IS NOT INPUT 
while True:
  num=input("Enter any integer or type stop to terminate: ")
  if num.lower() == "stop":
    break
  n = int(num)
print("your last input is  ",n)
