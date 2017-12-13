from math import gcd

def part1(input):
    return sum(x * input[x] for x in input if not x % (input[x] * 2 - 2))
    
def part2(input):
    cycles = {}
    for x in input:
        try:
            cycles[input[x] * 2 - 2].add(-x % (input[x] * 2 - 2))
        except KeyError:
            cycles[input[x] * 2 - 2] = {-x % (input[x] * 2 - 2)}
    lcm = 1
    res = {0}
    for divisor in cycles:
        old = lcm
        lcm *= divisor // gcd(divisor, lcm)
        res = {x for x in {z for y in res for z in range(y, lcm, old)} if x % divisor not in cycles[divisor]}
    return min(res)

def main():
    input = open('day13.txt').read().replace('\n', ', ')
    eval('print(part1({%s}), part2({%s}))' % (input, input))
    
if __name__=='__main__':
    main()
    