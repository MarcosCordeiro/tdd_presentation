def factorial(number):

    if(type(number)!=int):
        raise ValueError('Invalid Input')

    if(number==0):
        return 1

    if(number<1):
        return 0
    
    return  number * factorial(number -1)
