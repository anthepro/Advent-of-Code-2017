def part12(input, start):
    moves = {'left': (0, -1), 'right': (0, 1), 'down': (1, 0), 'up': (-1, 0)}
    opposite = {'left': 'right', 'right': 'left', 'down':'up', 'up': 'down'}
    pos = (0, start)
    direction = 'down'
    res = []
    cnt = 0
    while input[pos] != ' ':
        if input[pos] == '+':
            direction = next(x for x in moves if input[tuple(map(sum, zip(moves[x], pos)))] != ' ' and x != opposite[direction])
        elif input[pos] != '-' and input[pos] != '|':
            res.append(input[pos])
        pos = tuple(map(sum, zip(moves[direction], pos)))
        cnt += 1
    return ''.join(res), cnt

def main():
    input = open('day19.txt').read().split('\n')
    print(*part12({(x, y): char for x, line in enumerate(input) for y, char in enumerate(line)}, input[0].index('|')))
    
if __name__=='__main__':
    main()