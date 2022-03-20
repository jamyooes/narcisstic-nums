"""
Author: James Yoo
Problem: Narcisstistic Number
"""

"""
This is a function to print all anrcisstic number until the nth narcisstic number. 
A brute force method

param: expects an integer 
return: None
"""
def narc(nth_number):
    narc_list = []
    increment = 0
    while len(narc_list) < nth_number:
        if (is_narc(increment)):
            narc_list.append(increment)
        increment += 1
    print (narc_list) 


"""
This is a function to check if the number is a narcisstic number

param: expects an integer
return: returns true if the number is narcisstic 
        returns false if the number is not narcisstic
"""
def is_narc(number):
    length_number = len(str(number))    
    number = str(number)
    sum_narcisstic = 0

    for digit in number:
        sum_narcisstic += int(digit) ** length_number

    if int(number) == sum_narcisstic:
        return True

    return False

"""
This is a function to print out narcisstic numbers until a specified number

param: expects an integer
return: returns an array of narcisstic numbers
"""
def until_narc(number):
    narc_list = []
    for i in range (number + 1):
        if (is_narc(increment)):
            narc_list.append(increment)
    return narc_list

"""
This is to test code 
"""
if __name__ == "__main__":
    narc(20) #look for the nth narcisstic number (tip don't do any number larger than 89 because there is only 89 narcisstic numbers in base 10)
    is_narc(7) #check whether some number is a narcisstic number or not
    until_narc(89) #look for all narcisstic numbers until some number