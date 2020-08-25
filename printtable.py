def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

def powertable(power, stop):
    """
    Prints the powers of i from 1 to
    including <stop> using <power>
    as power term
    """
    for i in range (1, stop+1):
        print(i**power)

if __name__ == '__main__:
    multtable(1, 4, 7)
    powertable(2,4)
