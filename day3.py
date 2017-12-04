from math import floor, pow, sqrt

def steps(number):
    distance = floor(sqrt(number))
    distance -= 1 if distance % 2 == 0 else 0
    cyclepos = (number - pow(distance, 2)) % (distance + 1)
    return  abs(cyclepos - ((distance + 1)/2)) + (distance + 1)/2

def main():
    print(steps(347991))
    
if __name__=='__main__':
    main()

#part2: https://oeis.org/A141481