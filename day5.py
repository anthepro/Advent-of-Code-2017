#i assumed that the first index out of bounds would be positive and it appears
#that i was right. a negative index would also be a valid solution, but wouldn't
#raise an exception. might not work for your case, but it probably will

def part1(input):
    cnt = 0
    pos = 0
    while(True):
        try:
            input[pos] += 1
            pos += input[pos] - 1
            cnt += 1
        except IndexError:
            return cnt
            
def part2(input):
    cnt = 0
    pos = 0
    while(True):
        try:
            tmp = input[pos]
            input[pos] += 1 if input[pos] < 3 else -1
            pos += tmp
            cnt += 1
        except IndexError:
            return cnt

def main():
    input = [int(x) for x in open('day5.txt')]
    print(part1(input[:]), part2(input))
    
if __name__=='__main__':
    main()