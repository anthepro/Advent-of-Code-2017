def cycle(banks):
    seen = []
    cnt = 0
    while banks not in seen:
        seen.append(banks[:])
        cnt += 1
        index = banks.index(max(banks))
        for x in range(banks[index]):
            banks[(index + 1 + x) % 16] += 1
        else:
            banks[index] -= x + 1
    return cnt, len(seen) - seen.index(banks) #easiestpart2ever

def main():
    start = [int(x) for x in '5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6'.split()]
    print(cycle(start))
    
if __name__=='__main__':
    main()