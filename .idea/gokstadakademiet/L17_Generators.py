
def positive_integers():
    n = 1
    count = 0;

    while count<5:
        yield n
        n += 1
        count += 1

generate = positive_integers()
print(generate)         #<generator object positive_integers at 0x000001ACF0088040>

for num in generate:
    print(num)


print("-------------------------------------------------------------------------------------")


#genererer tallene fra n til 10
def even_numbers():
    n = 2
    while n<=10:
        yield n
        n += 2
gen = even_numbers()

for num in gen:
    print(num)


print("-------------------------------------------------------------------------------------")

#generer de fem første kvadrattallene
def square_numbers():
    n = 1
    count = 0

    while count<5:
        yield n ** 2
        n += 1
        count += 1
gen = square_numbers()

for num in gen:
    print(num)


print("-------------------------------------------------------------------------------------")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_generator():
    n = 2
    count = 0
    while count < 5:
        if is_prime(n):
            yield n
            count += 1
        n += 1

gen = prime_generator()

for prime in gen:
    print(prime)
