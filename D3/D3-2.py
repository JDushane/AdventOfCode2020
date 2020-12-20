def scan(file, x, y):
    position = 0
    lineNumber = 1
    hits = 0

    for line in file:
        lineNumber += 1
        
        if lineNumber % y == 0:
            
            line = line.rstrip()
            
            if line[position % len(line)] == '#': #This is the proper way, removes subtraction error
                hits += 1
            
            position += x

    return hits

if __name__ == '__main__':
    input = open("/home/j/Code/AOC2020/D3/D3input.txt")
    
    print(scan(input, 1, 1))
    input.seek(0)
    
    print(scan(input, 3, 1))
    input.seek(0)

    print(scan(input, 5, 1))
    input.seek(0)

    print(scan(input, 7, 1))
    input.seek(0)

    print(scan(input, 1, 2))