def part12(input):
    components = {tuple(int(y) for y in x.split('/')) for x in input}
    bridges = {(x, ) for x in components if 0 in x}
    strength = {x: sum(*x) for x in bridges}
    longest = (0, 0)
    while bridges:
        x = bridges.pop()
        port = next(y for y in x[0] if y != 0) if len(x) == 1 else x[-1][0] if x[-1][0] not in x[-2] else x[-1][1]
        end = True
        for y in components - set(x):
            if port in y:
                new = x + (y, )
                bridges |= {new}
                strength[new] = strength[x] + sum(y)
                end = False
        if end:
            longest = (longest, (len(x), x))[len(x)>longest[0] or len(x)==longest[0] and strength[longest[1]]<strength[x]]
    return max(strength.values()), strength[longest[1]]

def main():
    print(*part12(open('day24.txt').read().split('\n')))
    
if __name__=='__main__':
    main()