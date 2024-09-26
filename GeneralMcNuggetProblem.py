# isAccessable(x, a, b, knownAccessables)
#   x is a positive integer to be verified
#   a is a positive integer 
#   b is a positive integer larger than a 
#   knownAccessables is a list of integers that are accessable from a and b 
def isAccessable(x, a, b, knownAccessables):
    if(x % a == 0): return True
    if(x % b == 0): return True
    if((x - a) in knownAccessables): return True
    if((x - b) in knownAccessables): return True
    return False

# generalMcNugget takes in two positive integers
#   two positive integers, smallerInt and largerInt
#   where the GCD of smallerInt and largerInt is 1
#   Returns the highest integer not accessable by a sum of factors of those integers
#   e.g. the highest number of Chicken McNuggets you can't buy at a McDonald's
def generalMcNugget(smallerInt, largerInt):
    if(largerInt % smallerInt == 0):
        return -1
    
    i = smallerInt
    highest_inaccessable = smallerInt - 1
    accessables = [smallerInt]
    countdown = smallerInt
    
    # The loop can terminate once we've found x accessable values in a row 
    #   because after that point any number can be reached by taking a value 
    #   from that stretch and adding some factor of x
    while(countdown > 0):
        if (isAccessable(i, smallerInt, largerInt, accessables)):
            print(f'the number {i} is accessable!')
            accessables.append(i)
            countdown -= 1
        else:
            print(f'the number {i} is not accessable!')
            highest_inaccessable = i
            countdown = smallerInt
        i += 1
    
    return highest_inaccessable

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'The highest number inaccessable between {a} and {b} is...')
print(generalMcNugget(a,b))