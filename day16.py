def part1(input, programs):
    for x in input:
        if x[0] == 's':
            programs = programs[-int(x[1:]):] + programs[:-int(x[1:])]
        elif x[0] == 'x':
            first, second = map(int, x[1:].split('/'))
            programs[first], programs[second] = programs[second], programs[first]
        else:
            first, second = map(programs.index, x[1:].split('/'))
            programs[first], programs[second] = programs[second], programs[first]
    return programs

def part2(input):
    programs = [chr(x + 97) for x in range(16)]
    for cnt in range(1000000000):
        if programs == [chr(x + 97) for x in range(16)] and cnt:
            break
        programs = part1(input, programs)
    for _ in range(1000000000 % cnt):
        programs = part1(input, programs)
    return ''.join(programs)

def main():
    input = open('day16.txt').read().split(',')
    print(''.join(part1(input, [chr(x + 97) for x in range(16)])), part2(input))

if __name__=='__main__':
    main()