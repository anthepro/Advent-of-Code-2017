'''When deciding between performance and readability, choose readability'''

def generator(value, multiplier):
    while True:
        value = value * multiplier % 2147483647
        yield value

def condition(value, multiplier, condition):
    gen = generator(value, multiplier)
    for val in gen:
        if not val % condition:
            yield val

def part1():
    genA = generator(591, 16807)
    genB = generator(393, 48271)
    return sum(not (next(genA) ^ next(genB)) & 65535 for _ in range(40000000))
    
def part2():
    genA = condition(591, 16807, 4)
    genB = condition(393, 48271, 8)
    return sum(not (next(genA) ^ next(genB)) & 65535 for _ in range(5000000))
    
def main():
    print(part1(), part2())
    
if __name__=='__main__':
    main()
