x = [[]] * 3

x[0].append(1)

print(x)

# ACTUAL OUTPUT IS [[1], [1], [1]]
"""WHY THIS HAPPENS
x = [[]] * 3

It does NOT create 3 separate lists.

Instead, it creates 3 references to the SAME list in memory.
🔥 When :
x[0].append(1)

It  modifyes the same list, so all appear changed."""