def part1(input):
    """Copy paste from the other day, lame."""
    registers = {chr(x + 97): 0 for x in range(8)}
    pos = 0
    cnt = 0
    while pos < len(input):
        x = input[pos].split()
        if x[0] == 'jnz':
            if x[1] in registers:
                if not registers[x[1]]:
                    pos += 1
                    continue
            elif int(x[1]) <= 0:
                pos += 1
                continue
            pos += registers[x[2]] if x[2] in registers else int(x[2])
            continue
        elif x[0] == 'set':
            registers[x[1]] = registers[x[2]] if x[2] in registers else int(x[2])
        elif x[0] == 'sub':
            registers[x[1]] -= registers[x[2]] if x[2] in registers else int(x[2])
        else:
            registers[x[1]] *= registers[x[2]] if x[2] in registers else int(x[2])
            cnt += 1
        pos += 1
    return cnt

def part2():
    """
    And some mean people didn't believe keeping a 200GB file of primes
    at hand would eventually pay off! Adding only a small piece of that file
    to repo (enough for this), because uploading a 200GB file would
    take forever with my crappy connection.
    """
    cnt = len(range(108100, 125101, 17))
    with open('D:\Documents\primes.txt', 'r') as primes:
        while True:
            x = int(primes.readline())
            if x > 125100:
                break
            if x in range(108100, 125101, 17):
                cnt -= 1
    return cnt

def main():
    input = open('day23.txt').read().split('\n')
    print(part1(input), part2())

if __name__=='__main__':
    main()