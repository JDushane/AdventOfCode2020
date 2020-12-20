#find the three entries that sum to 2020 and then multiply those numbers together.

def scan(file):
    data = []
    for line in file:
        data.append(line.strip('\n'))


    for i in range(0, len(data)):
        x = int(data[i])
        for j in range(i + 1, len(data)):
            y = int(data[j])
            for k in range(j+1, len(data)):
                z = int(data[k])
                if x + y + z == 2020:
                    return x * y * z #This could get messy if more needed


if __name__ == "__main__":
    file = open("D1Input.txt")
    
    print(scan(file))
    
    file.close()