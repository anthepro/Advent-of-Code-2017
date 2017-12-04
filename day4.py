def part1():
    return sum(len(x.split()) == len(set(x.split())) for x in open('day4.txt'))

def part2():
    return sum(len(x.split()) == len(set([''.join(sorted(y)) for y in x.split()])) for x in open('day4.txt'))
    
def main():
    print(part1(), part2())
    
if __name__=='__main__':
    main()