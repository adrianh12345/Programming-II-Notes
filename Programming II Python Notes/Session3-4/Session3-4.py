# eratosthenes method
# compile the first n numbers into a list. #= assigns a value, and == equals
x = list(range(2, n+1)) # generates an x-sequence beginning at 2 since prime numbers are integers larger than 1.

    for i in x: # checks if each number i in the list x is a prime number by iterating over each one.
    j = 2 # counts in i*j or 2 increments
    while (i * j <= x[-1]): # continues until the product of i*j is equal to or less than the list's final number.
        if (i * j in x): # see if i*j belongs in sequence x.
            x.remove(i*j) # Should that be the case. It's eliminated since it indicates that i*j is a multiple of i and not a prime number.
    j += 1 # += and =j+1 are equivalent.
    # To verify the next multiple in the while loop's subsequent iteration, j is increased by 1.
print("the list of prime numbers is:", x) #final list of numbers up to n is produced.