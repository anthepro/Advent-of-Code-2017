def part1(input):
    minacc = min(sum(abs(y) for y in input[x][2]) for x in input)
    tied = (x for x in input if sum(abs(y) for y in input[x][2]) == minacc)
    return min(tied, key=lambda x: sum(y * z for y, z  in zip(input[x][1], input[x][2])))

def part2(input):
    """
    I have no idea when to stop the loop, so I just stop it manually
    when I see the value has stopped changing, just Ctrl+C
    """
    position = {x: input[x][0] for x in input}
    velocity = {x: input[x][1] for x in input}
    try:
        while True:
            velocity = {x: tuple(map(sum, zip(velocity[x], input[x][2]))) for x in position}
            position = {x: tuple(map(sum, zip(position[x], velocity[x]))) for x in position if tuple(position.values()).count(position[x]) == 1}
            print(len(position))
    except KeyboardInterrupt:
        return len(position)

def main():
    input = {x: (tuple(map(int, y.split(',')[:3])), tuple(map(int, y.split(',')[3:6])), tuple(map(int, y.split(',')[6:]))) for x, y in enumerate(open('day20.txt').read().translate({ord(y):'' for y in ' pav=<>'}).split('\n'))}
    print(part1(input), part2(input))
    
if __name__=='__main__':
    main()
