# PROGRAM TOO GREET ACCORDING TO TIME
import time
a=time.strftime('%h:%m:%S:%H:%M:%S')
print(a)
t=int(time.strftime("%H"))
if t>0 and t<12:
    print("GOOD MORNING !!")
elif t>=12 and t<17:
    print("GOOD AFTERNOON !!")
elif t>=17 and t<=24:
    print("GOOD EVENING !!")
