def checksum(table):
    return sum((max(x) - min(x)) for x in table)
    
def checksum2(table):
    return sum(a//b for x in table for a in x for b in x if not (a % b) and a != b)

def main():
    table = [[int(y) for y in x.split('\t')] for x in open('day2.txt')]
    print(checksum(table), checksum2(table))
    
if __name__=='__main__':
    main()
