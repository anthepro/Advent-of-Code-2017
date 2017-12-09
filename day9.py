import re

def part1():
    input = [1 if x == '{' else -1 for x in re.sub(r'<[^>]*>' , '', re.sub(r'!.', '', open('day9.txt').read())).replace(',', '')]
    return sum(sum(input[:x+1]) for x in range(len(input)) if input[x] == 1)

def part2():
    return len(''.join(re.findall(r'<([^>]*)>', re.sub(r'!.', '', open('day9.txt').read()))))

def main():
    print(part1(), part2())
    
if __name__=='__main__':
    main()
    