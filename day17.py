def part1(step):
    spinlock = [0]
    pos = 0
    for x in range(2017):
        pos = (pos + step + 1) % (x + 1)
        spinlock.insert(pos, x + 1)
    return print(spinlock[(spinlock.index(2017)+1)%(x+2)]), (spinlock.index(0)+1) % (x + 2)

def part2(step):
    pos = 0
    res = 0
    _, target = part1(step)
    x = 0
    while x < 50000000:
        skip = max(1, (x - pos) // step)
        x += skip
        pos = (pos + skip * (step + 1)) % (x + 1)
        if pos == target:
            res = x + 1
    return res

def main():
    print(part2(367))

if __name__=='__main__':
    main()
