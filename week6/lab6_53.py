# 5.3 Create in Python the program containing a function, called report, which creates a
# short report of the quantities of spare parts sold in three different stores (located in London, Birmingham
# and Nottingham). The function:
# espectively, in London, Birmingham and Nottingham.
# old in London, € 57 for those sold in Birmingham and € 59 for those sold in Nottingham.
# S receives three mandatory parameters (q1, q2 and q3) containing the quantities sold,
#create a report similar to the example shown below, showing two decimal digits for renues
# receives three optional parameters containing the price of the spare parts: € 60 for spare parts
# calculates the revenue of each store, the average quantity sold and the average revenue


def report(q1,q2,q3,price1=60,price2=57,price3=59):
    avg_revenue = ((q1*price1)+(q2*price2)+(q3*price3))/3
    print(f"{'Store':<15}{'Quantity':<10}{'Revenue [£]'}")
    print(f"{'London':<15}{q1:<10}{q1*price1:>10.2f}")
    print(f"{'Birmingham':<15}{q2:<10}{q2*price2:>10.2f}")
    print(f"{'Nottingham':<15}{q3:<10}{q3*price3:>10.2f}")
    print(f"{'MEAN':<15}{avg_revenue:<10.1f}{avg_revenue:>10.2f}")
#----------main program----------------
london_quantity = int(input("Enter quqntity sold in London: "))
brimingham_quantity =int(input("Enter the quqntity sold in Brimingham: "))
nottingham_quantity = int(input("Enter the quantity sold in Nottingham: "))

# function calling
report(london_quantity,brimingham_quantity,nottingham_quantity)
print("\n")