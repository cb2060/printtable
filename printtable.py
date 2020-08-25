def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

def powertable(power, stop):
	"""
	Print the numbers from 1 to including <stop>
	raised to the power of <power>
	"""
	for i in range(1, stop+1):
		print(i**power)
