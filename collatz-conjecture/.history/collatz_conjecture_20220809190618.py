def steps(number):
    
    counter = 0
    
    if number == 0 or number < 0:
        raise ValueError("Number must be positive")
    

    while not number == 1:
        
        counter+=1

        if number%2 == 0:
            number = number/2
        
        if number

