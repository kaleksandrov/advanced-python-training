# TODO

# 1. Createagenerator
# 2. Yields a factorial starting at 1!
# 3. Each iteration yields the next factorial ( 2!, 3!, and so on)
# 4. Test generator
# 5. Create an iterator that calculates a factorial to a set value, such as 5! or 7!
# 6. Test with a for statement


def fact(n):
    total = 1
    for i in range(1, n+1):
        total *= i
        yield total

gen = fact(9)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


class Factorial(object):


    def __init__(self, number):
        self.number = number


    def __iter__(self):
        return Iterator(self.number)


class Iterator(object):

    def __init__(self, number):
        self.total = 1
        self.current = 1
        self.number = number


    def __next__(self):
        self.total *= self.current

        if(self.current > self.number):
            raise StopIteration()

        self.current += 1
        return self.total


print(10*'=')

for i in Factorial(9):
    print(i)
