def fileAdd(file1):
    #reads text file, converts to a list of numbers, returns sum
    numbers = []

    #open file
    with open(file, 'r') as f:
        for line in f:
            #strip whitespace and convert
            line = line.strip()
            if line: # skip empty line
                numbers.append(float(line))
        
        total = sum(numbers)
        return total


def main(): 
    total1 = fileAdd("file1.txt")
    print(total1)

    

    



