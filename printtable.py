def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

multtable(1, 4, 7)


def power(powernumber, number):
    """Lists all numbers to the power choosen as powernumber
    """
    for i in range(1, number+1):
        print(i**powernumber)

power(2,4)