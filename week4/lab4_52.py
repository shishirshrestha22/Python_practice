# THIS PROGRAM COUNTS THE NUMBER OF EVEN, ODD AND ZEROS IN A INTE
def digits(number):
    even_count = 0
    odd_count = 0
    zero_count = 0
    for digit in number:
        if digit == "0":
            zero_count += 1
        elif int (digit) % 2 ==0:
            even_count += 1
        else:
            odd_count +=1
    return  even_count, odd_count, zero_count  
number = input("Enter the number:")
even_count, odd_count,zero_count = digits(number)
print(even_count, odd_count, zero_count)
print("Number of even digits:", even_count)
print("Number of odd digits:", odd_count)
print("Number of zeros:", zero_count)
