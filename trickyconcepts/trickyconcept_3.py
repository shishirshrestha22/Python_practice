s = "hello"
for char in s:
    char = char.upper()

print(s)
# OUTPUT IS  "hello"
"""Reason : Strings are IMMUTABLE
In Python:
Strings cannot be changed after they are created.
So the string "hello" stored in variable (s) cannot be modified character-by-character.

When :
for char in s:
We get a copy of each character, not the real character in the string."""


#------------------------------------------------------
#BUT  we can get the Output "HELLO"  if:
for char in s:
    s = s.upper()
print(s)

#Output is "HELLO"

