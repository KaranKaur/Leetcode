"""

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output -  Fizz instead of the number and
for the multiples of five output  - Buzz.
For numbers which are multiples of both three and five output -  FizzBuzz.

"""
def fizzbuzz(n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

print(fizzbuzz(15))