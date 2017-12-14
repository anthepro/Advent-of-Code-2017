from day10 import part2 as knothash

def regions(grid, x, y):
    grid[x][y] = 0
    if x > 0 and grid[x-1][y]:
        regions(grid, x-1, y)
    if y > 0 and grid[x][y-1]:
        regions(grid, x, y-1)
    if x < 127 and grid[x+1][y]:
        regions(grid, x+1, y)
    if y < 127 and grid[x][y+1]:
        regions(grid, x, y+1)

def part12(input):
    grid = [[int(y) for y in format(int(knothash(input + [ord(z) for z in str(x)]), 16), '0>128b')] for x in range(128)]
    part1 = sum(sum(x) for x in grid)
    cnt = 0
    for x in range(128):
        for y in range(128):
            if grid[x][y]:
                cnt += 1
                regions(grid, x, y)
    return part1, cnt

def main():
    input = 'nbysizxe-' #appended - to input
    print(part12([(ord(x)) for x in input]))
    
if __name__=='__main__':
    main()
    