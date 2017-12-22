from collections import deque

def part1(input):
    pos = (len(input)//2, len(input[0])//2)
    dirs = deque(((-1, 0), (0, -1), (1, 0), (0, 1)))
    infected = {(x, y) for x, z in enumerate(input) for y, _ in enumerate(z) if input[x][y] == '#'}
    cnt = 0
    for _ in range(10000):
        if not pos in infected:
            dirs.rotate(-1)
            infected.add(pos)
            cnt += 1
        else:
            dirs.rotate(1)
            infected.remove(pos)
        pos = tuple(map(lambda x, y: x + y, dirs[0], pos))
    return cnt
    
def part2(input):
    pos = (len(input)//2, len(input[0])//2)
    dirs = deque(((-1, 0), (0, -1), (1, 0), (0, 1)))
    special = {(x, y): 'I' for x, z in enumerate(input) for y, _ in enumerate(z) if input[x][y] == '#'}
    cnt = 0
    for _ in range(10000000):
        if not pos in special:
            dirs.rotate(-1)
            special[pos] = 'W'
        else:
            if special[pos] == 'W':
                special[pos] = 'I'
                cnt += 1
            elif special[pos] == 'I':
                dirs.rotate(1)
                special[pos] = 'F'
            else:
                dirs.rotate(2)
                del special[pos]
        pos = tuple(map(lambda x, y: x + y, dirs[0], pos))
    return cnt
    
def main():
    input = [list(x) for x in open('day22.txt').read().split('\n')]
    print(part1(input), part2(input))
    
if __name__=='__main__':
    main()
