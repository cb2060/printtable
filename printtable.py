def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")




def powertable(power,num):
    for i in range(1,num+1):
        p = (i)**power
        print(p)
if __name__ == '__main__':
    multtable(1, 4, 7)
    powertable(2,4)

