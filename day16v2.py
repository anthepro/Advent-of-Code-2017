"""A much better solution for day16"""

def dance(input, target):
    indexes = [x for x in range(16)]
    programs = [chr(x + 97) for x in indexes]
    partners = {x: x for x in programs}
    for x in input:
        if x[0] == 's':
            indexes = indexes[-int(x[1:]):] + indexes[:-int(x[1:])]
        elif x[0] == 'x':
            first, second = map(int, x[1:].split('/'))
            indexes[first], indexes[second] = indexes[second], indexes[first]
        else:
            first, second = x[1:].split('/')
            partners = {y: second if partners[y] == first else first if partners[y] == second else partners[y] for y in partners}
    while target:
        if target & 1:
            programs = [partners[programs[x]] for x in indexes]
        indexes = [indexes[x] for x in indexes]
        partners = {x: partners[partners[x]] for x in partners}
        target //= 2
    return ''.join(programs)

def main():
    input = open("day16.txt").read().split(',')
    print(dance(input, 1), dance(input, 1000000000))
    
if __name__=='__main__':
    main()
