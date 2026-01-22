
filename = "data.txt"

# Take input from user
name = input("Enter your name: ")
age = input("Enter your age: ")

# Open file in append mode
file = open(filename, "a")

# Write data to file
file.write(name + "," + age + "\n")

file.close()

print("\nData saved successfully!\n")

# Opens file in read mode
file = open(filename, "r")

# Read file line by line
print("---- File Content ----")
for line in file:
    print(line.strip())

# Close the file after reading
file.close()
