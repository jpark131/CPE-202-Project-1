
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    quo = num
    rem = ''
    new = ''
    if quo == 0: #base case
        new += str(rem)
        return new
    quo = num//b #dividing the quotient by the base
    rem = num%b #getting the remainder
    if b > 10: #number assignments for bases greater than 10
        if rem > 9:
            rem = chr(rem +55) #Ascii table conversions
    new = str(convert(quo,b)) + str(rem) #recursive call adding the remainders in reverse order
    return new

