# THIS SEEMS BASIC CONCEPT BUT MAY TRICKS WITH THE OUTPUT FOR THE FIRST TIME

a = "python"
if a == "java" or "javascript":
    print("Access granted")
else:
    print("Access denied")


#  In this program python actually parses this as:

# if (a == "java") or ("javascript"):

# ✔ Part 1

# a == "java"?
# Since a = "python", this is False.


# ✔ Part 2
# "javascript" by itself is a non-empty string, which is always treated as True in boolean context.

#Thus this condition becomes True every time
#so prints "true condtion part " even if the the variable != actual value 