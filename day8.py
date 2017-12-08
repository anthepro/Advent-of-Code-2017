import re

def part12():
    exec('registers = {}\nmaxx = 0\n%s\nprint(max(registers.values()), maxx)' % re.sub(r'([^ ]+)( [^ ]+[^i]+if )([^ ]+)([^\n]+)\n?',  r'''while True:\n    try:\n        registers['\1']\2registers['\3']\4 else 0\n        break\n    except KeyError as key:\n        registers[key.args[0]] = 0\nmaxx = max(maxx, registers['\1'])\n''', open('day8.txt', 'r').read()).replace('inc', '+=').replace('dec', '-='))

def main():
    part12()
    
if __name__=='__main__':
    main()