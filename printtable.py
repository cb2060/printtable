def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

def powertable(power,base):
	"""
	Takes the "base" as the base and "power" as the power as a formular: base^power 
	"""
	for j in range(1,base+1):
		print(f"{j}**{power}={j**power}")

if __name__ == '__main__':
    multtable(1, 4, 7)
    powertable(3,3)
