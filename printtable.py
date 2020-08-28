def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")
def powertable(pow_num,number):
    """
    Print numbers which from 1 to the <number+1> 
    to the power of pow_num
   
    """
    for i in range(1,number+1):
        print (i**pow_num)

if __name__ == '__main__':
    multtable(1, 4, 7)
    powertable(3,3)
