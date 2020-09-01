def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

if __name__ == '__main__':
    multtable(1, 4, 7)



def powertable(power,numbers):
    for i in range(1,numbers+1):
        print(i**power)

powertable(2,4)
