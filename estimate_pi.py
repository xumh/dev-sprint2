def factorial(n):
    if n == 0:
    	return 1
    else:
    	recurse = factorial(n-1)
    	result = n * recurse
    	return result

def estimate_pi():
    """Computes an estimate of pi.

    Algorithm due to Srinivasa Ramanujan, from 
    http://en.wikipedia.org/wiki/Pi
    """
    k = 0
    top = factorial(4 * k) * (1103+26390 * k)
    down = (factorial(k) **4 )* 396**(4 * k)
    left = (2 * 2**0.5)/9801
    term = left * top/down
    ## why abs(term)??
    while term >= 1e-15:
    	k = k+1
    	term = term + estimate_pi(k)
    smpi = 1/ term
    print smpi

#testing Chap8
import string
letters = string.ascii_lowercase
    index = 0
    while index < len(anyword):
        pos = letters.find(anyword[index])
        newpos = pos + nm
        if newpos > 25:
            newpos = newpos - 26
        newletter = letters[newpos]

        

#print rotate_word('cheer', 7)