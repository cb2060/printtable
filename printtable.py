def multtable(start, stop, number):
    """
    Print power <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} ^ {number} = {i**number}")

multtable(1, 7, 2)
