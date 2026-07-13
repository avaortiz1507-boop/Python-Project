

def fizz_buzz(number):
    results = []

    for index in range(1, number + 1):
        if index % 3 == 0 and index % 5 == 0:
            results.append("FizzBuzz")
        elif index % 3 == 0:
            results.append("Fizz")
        elif index % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(index))

    return results

n = 10
print(fizz_buzz(n))

# make a loop that for numbers that is divisible by 3. if so print "Fizz"; 

    # make a loop that for numbers that is divisible by 5. if so print "Buzz"; 

    # make a loop that for numbers that is divisible 3 and 5. if print "FizzBuzz"; 
  
    # if the number is not divisible by either 3 or 5, print the number itself