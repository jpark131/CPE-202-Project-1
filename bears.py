def bears(n):
    """A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
     bears."""
    if n == 42: #checks if the target number has been reached
        return True
    if n < 42: #checks if the current number of bears is below the target
        return False
    if n%2 == 0: #checks if n is divisible by two
        new = n//2
        if bears(new): #recursive call on the new number of bears
            return True
    if n%5 == 0: #checks if n is divisible by five
        new = n - 42
        if bears(new): #recursive call on the new number of bears
            return True
    if n%3 or n%4 == 0: #checks if n is divisible by three or four
        mult = int(str(n)[len(str(n)) - 1]) * int(str(n)[len(str(n)) - 2]) #multiplying the last two digits of the integer
        if mult == 0:
            return False
        new = n - mult
        if bears(new): #recursive call on the new number of bears
            return True
    return False
