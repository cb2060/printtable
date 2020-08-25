def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

def powertable(base, last_exp, first_exp = 0):
    """
    Print power table for <base>
    from <first_exp> (by default, 0) to <last_exp>
    """
    for i in range (first_exp, last_exp + 1):
        print(f"{base} to the power of {i} = {base**i}")

if __name__ == '__main__':
    multtable(1, 4, 7)
