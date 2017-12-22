def rotate(grid):
    return tuple(''.join(x) for x in zip(*grid[::-1]))
    
def horizontalflip(grid):
    return tuple(x[::-1] for x in grid)

def create_rulebook():
    rulebook = {}
    for x in open('day21.txt').read().split('\n'):
        key, value = tuple(tuple(y.split('/')) for y in x.split(' => '))
        for _ in range(4):
            key = rotate(key)
            rulebook[key] = value
            rulebook[horizontalflip(key)] = value
    return rulebook

def enhance(grids, rulebook):
    return (rulebook[x] for x in grids)

def part12(rulebook, iterations):
    grids = [('.#.', '..#', '###')]
    for cnt in range(iterations):
        if not cnt % 3:
            grids = [''.join(x) for x in enhance(grids, rulebook)]
        elif cnt % 3 == 1:
            for num, grid in enumerate(grids):
                grid = tuple((grid[x:x+2], grid[x+4:x+6]) for y in range(0, 16, 8) for x in range(y, y+4, 2))
                grids[num] = ''.join(''.join(('%s%s' % (y[x], y[x+1])) for y in zip(*enhance(grid, rulebook))) for x in range(0, 4, 2))
        else:
            for num, grid in enumerate(grids):
                grid = tuple((grid[x:x+2], grid[x+6:x+8]) for y in range(0, 36, 12) for x in range(y, y+6, 2))
                grids[num] = enhance(grid, rulebook)
            grids = [y for x in grids for y in x]
    return sum(sum(1 if z == '#' else 0 for z in y) for x in grids for y in x)

def main():
    rulebook = create_rulebook()
    print(part12(rulebook, 5), part12(rulebook, 18))
    
if __name__=='__main__':
    main()
