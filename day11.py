"""The magic of today's code requires some explanations"""

def part1(input):
    """
    this seems to be working, but it could be wrong, i'll just quote Hüsker Dü:
    It could be good, and it could be bad
    I don't know for sure
    """
    return max(abs(sum(1 if x == 'ne' else -1 if x == 'sw' else 0 for x in input)), abs(sum(1 if x == 'nw' else -1 if x == 'se' else 0 for x in input))) + abs(sum(1 if x == 'n' else -1 if x == 's' else 0 for x in input))
    
def part2(input):
    """Very slow, but clean code + using part1 so why not"""
    return max(part1(input[:x+1]) for x in range(len(input)))

def main():
    input = open('day11.txt').read().split(',')
    print(part1(input), part2(input))

if __name__=='__main__':
    main()
    