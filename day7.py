import re
import timeit

def part1():
    return set([x.split()[0] for x in open('day7.txt')]) - set([x.strip() for y in open('day7.txt') if '->' in y for x in y.split('->')[1].split(',')])
    
def part2():
    with open('day7.txt', 'r') as file:
        text = file.read()
    regex = re.findall(r'([^ ]+)[^\d]+([^)]+)[^a-z|\n]+([^\n]+)?\n?', text)
    children = {x[0]: x[2].replace(' ', '').split(',') for x in regex}
    parent = {y.strip(): x[0] for x in regex for y in x[2].split(',')}
    weights = {x[0]: int(x[1]) for x in regex}
    done = {x[0]: int(x[1]) for x in regex if not x[2]}
    names = [parent[x] for x in done]
    while True:
        for x in names:
            if x in children and not bool(set(children[x]) & set(names)):
                if len(set([done[y] for y in children[x]])) != 1:
                    suspects = [done[y] for y in children[x]]
                    return weights[{done[y]: y for y in children[x]}[min(set(suspects), key=suspects.count)]] - (min(set(suspects), key=suspects.count) - max(set(suspects), key=suspects.count))
                done[x] = sum(done[y] for y in children[x]) + weights[x]
                names.remove(x)
                names.append(parent[x])

def main():
    print(part1(), part2())
    
if __name__=='__main__':
    main()
