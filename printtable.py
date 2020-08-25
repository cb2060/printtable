def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

multtable(1, 4, 7)

def powertable(power,num):
    for i in range(1,num+1):
        p = (i)**power
        print(p)

powertable(2,4)

