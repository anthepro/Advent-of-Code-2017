"""
I was rushing a solution to get on the leaderboard because I happened to 
be awake at an ungodly hour, so the code is somewhat uglier than usual. 
Had a 15min handicap because I was playing League of Legends, my stats:

    Part1: 00:24:17    312      0  Part2: 00:37:05     74     27

Not bad! Probably would've been a much higher spot had I started on time and 
had I not made a typo twice when entering the result of part2. No part1 
because I just edited the part1 code for part2.
"""

from multiprocessing import Process, Queue

def part1(input, id, queue):
    registers = {chr(x + 97): 0 for x in range(16)}
    registers['p'] = id
    pos = 0
    cnt = 0
    while pos < len(input):
        x = input[pos].split()
        if x[0] == 'jgz':
            if x[1] in registers:
                if registers[x[1]] <= 0:
                    pos += 1
                    continue
            elif int(x[1]) <= 0:
                pos += 1
                continue
            pos += registers[x[2]] if x[2] in registers else int(x[2])
            continue
        elif x[0] == 'set':
            registers[x[1]] = registers[x[2]] if x[2] in registers else int(x[2])
        elif x[0] == 'snd':
            queue[id].put(registers[x[1]] if x[1] in registers else int(x[1]))
            cnt += id
        elif x[0] == 'add':
            registers[x[1]] += registers[x[2]] if x[2] in registers else int(x[2])
        elif x[0] == 'mul':
            registers[x[1]] *= registers[x[2]] if x[2] in registers else int(x[2])
        elif x[0] == 'mod':
            registers[x[1]] %= registers[x[2]] if x[2] in registers else int(x[2])
        else:
            try:
                registers[x[1]] = queue[id-1].get(timeout=1)
            except:
                if id:
                    print(cnt)
                return
        pos += 1

def main():
    queue = [Queue(), Queue()]
    input = open('day18.txt').read().split('\n')
    first = Process(target=part1, args=(input, 0, queue))
    second = Process(target=part1, args=(input, 1, queue))
    first.start()
    second.start()
    first.join()
    second.join()
    
    
if __name__=='__main__':
    main()
