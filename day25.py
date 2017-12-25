def part1():
    machine = {('A', 0): ('B', 1, 1), ('A', 1): ('C', 1, 0), ('B', 0): ('A', -1, 0), ('B', 1): ('D', 1, 0), ('C', 0): ('D', 1, 1), ('C', 1): ('A', 1, 1), ('D', 0): ('E', -1, 1), ('D', 1): ('D', -1, 0), ('E', 0): ('F', 1, 1), ('E', 1): ('B', -1, 1), ('F', 0): ('A', 1, 1), ('F', 1): ('E', 1, 1)}
    tape = {}
    state = 'A'
    pos = 0
    for _ in range(12368930):
        state, move, tape[pos] = machine[(state, tape[pos] if pos in tape else 0)]
        pos += move
    return sum(tape.values())

def main():
    print(part1())
    
if __name__=='__main__':
    main()