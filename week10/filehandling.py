#this is program which is based on simple file handling concepts

file = open("data.txt","w")#----------------------------->>>> open() is used to open a file , data.txt is the file name
file.write("HEllo this is my first file handling python program")#------>> write() writes the text into file
file.close()#--------------->> closes the file an saves the data 

file = open("data.txt","r")#---------->>opens the file and r is the reading mode of the file
content = file.read()#-------->> creates content as new variable and reads the file 
print(content)
file.close()