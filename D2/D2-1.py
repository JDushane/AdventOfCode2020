#Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear.
#How many passwords are valid according to their policies?

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
    ruleCount = 0
        
    for char in pw:
        if char == rule:
            ruleCount += 1
    
    if ruleCount <= maximum and ruleCount >= minimum:
        return True
    else:
        return False

if __name__ == "__main__":
    input = open("/home/j/Code/AOC2020/D2/D2input.txt")
    
    print(scan(input))