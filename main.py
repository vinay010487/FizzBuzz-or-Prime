def isPrime(n):
    return n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# FizzBuzz loop
for counter in range(1, 101):
    output = ""
    if isPrime(counter):
        output += "Prime"
    else:
        if counter % 3 == 0:
            output += "Fizz"
        if counter % 5 == 0:
            output += "Buzz"
    print(output if len(output) else counter)
  