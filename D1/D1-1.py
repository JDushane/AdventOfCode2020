#find the two entries that sum to 2020 and then multiply those two numbers together.

def scan(file):
    data = []
    for line in file:
        data.append(line.strip('\n'))


    for i in range(0, len(data)):
        x = int(data[i])
        for j in range(i + 1, len(data)):
            y = int(data[j])
            if x + y == 2020:
                return x * y


if __name__ == "__main__":
    file = open("D1Input.txt")
    
    print(scan(file))
    
    file.close()