def multtable(start, stop, number):
    """Print multiplication table for <number> from <start> to including <stop> """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")



def powertable(power, stop):
 	"""Print powertable using the <power> exponent for consecutive bases from 1 to <stop>"""
 	for i in range(1, stop+1):
 		a = i**power
 		print(a)

if __name__ == '__main__':
	powertable(2, 4)
	powertable(3, 3)