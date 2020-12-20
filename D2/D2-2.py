#
def scan(file):
    goodPass = 0
    for line in file:
        if passwordGood(line):
            goodPass += 1
            
    return goodPass

def passwordGood(line):
    #6-8 s: svsssszslpsp
    code = line.split()
    rule = code[1][0]
    pw = code[2]
    
    amounts = code[0].split('-')
    minimum = int(amounts[0])
    maximum = int(amounts[1])
    
    if pw[minimum -1] == rule and pw[maximum -1] == rule:
        return False
    
    if pw[minimum -1] == rule:
        return True
    
    if pw[maximum -1] == rule:
        return True

if __name__ == "__main__":
    input = open("/home/j/Code/AOC2020/D2/D2input.txt")
    
    print(scan(input))