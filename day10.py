from functools import reduce

def part1(input):
    numbers = [x for x in range(256)]
    pos = 0
    for skip, length in enumerate(input):
        for x in range(length//2):
            numbers[(pos+x)%256], numbers[(pos+(length-x-1))%256] = numbers[(pos+(length-x-1))%256], numbers[(pos+x)%256]
        pos += length + skip
    return numbers[0] * numbers[1]
    
def part2(input):
    input.extend([17, 31, 73, 47, 23])
    numbers = [x for x in range(256)]
    pos = 0
    for a in range(64):
        for skip, length in enumerate(input):
            for x in range(length//2):
                numbers[(pos+x)%256], numbers[(pos+(length-x-1))%256] = numbers[(pos+(length-x-1))%256], numbers[(pos+x)%256]
            pos += length + skip + a * len(input)
    return ''.join(hex(reduce(lambda x, y: x ^ y, numbers[a*16:(a+1)*16]))[2:] for a in range(16))

def main():
    input = '129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108'
    print(part1([int(x) for x in input.split(',')]), part2([(ord(x)) for x in input]))
    
if __name__=='__main__':
    main()
    