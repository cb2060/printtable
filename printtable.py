def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop>
    """
    print ('Mult table')
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")
    print ('')
        #output: 1 x 7 = 7

def powertable(power, i):
    """
    Prints power table for <i> to the power of <power>
    """
    print ('Power table')
    for x in range (1, i + 1):
        print (f"{i} ^ {power} = {i**power}")
    print ('')

if __name__ == '__main__':
    multtable(1, 4, 7)
    powertable(2, 4)

#added under branch powers! -ashwini
