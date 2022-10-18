"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if number_of_primes <= 0:
        raise ValueError

    list = [2]
    i = 3
    while len(list) < number_of_primes:
        prime = True
        for j in list:
            if i%j == 0:
                prime = False
                break
        if prime:
            list.append(i)
        i += 2
    print(list)
    return list