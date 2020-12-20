def scan(file):
    position = 0
    hits = 0

    for line in file:
        line = line.rstrip()
        
        if line[position % len(line)] == '#': #This is the proper way, removes subtraction error
            hits += 1
        
        position += 3
        

    return hits


if __name__ == "__main__":
    input = open("/home/j/Code/AOC2020/D3/D3input.txt")
    
    print(scan(input))