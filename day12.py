def part12(pipes):
    cnt = 0
    while pipes:
        cnt += 1
        group = {next(iter(pipes))}
        old = {}
        while group != old:
            old = group.copy()
            group |= {y for x in group if x in pipes for y in pipes[x]}
        pipes = {x: pipes[x] for x in pipes if not pipes[x] <= group}
        if '0' in group:
            print(len(group))
    return cnt

def main():
    print(part12({x.split('<->')[0]: set(x.split('<->')[1].split(',')) for x in open('day12.txt').read().replace(' ', '').split('\n')}))
    
if __name__=='__main__':
    main()
