def powertable(power, number):
    '''
    prints power table for number in the power of "power"
    '''
    for i in range(1, number + 1):
        print(i ** power)
if __name__ == '__main__':
    powertable(2,4)
    powertable(3,3)
