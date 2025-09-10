import sys

def fileAdd(filename):
    #reads text file, converts to a list of numbers, returns sum
    numbers = []

    #open file
    with open(filename, 'r') as f:
        for line in f:
            #strip whitespace and convert
            line = line.strip()
            if line: # skip empty line
                numbers.append(float(line))
        
        total = sum(numbers)
        return total


def main(): 
    # Check if correct number of command line arguments provided
    if len(sys.argv) != 4:
        print("Usage: python main.py <file1> <file2> <file3>")
        print("Example: python main.py file1.txt file2.txt file3.txt")
        sys.exit(1)
    
    # Get command line arguments
    file1 = sys.argv[1]
    file2 = sys.argv[2] 
    file3 = sys.argv[3]
    
    print(f"Reading from: {file1} and {file2}")
    print(f"Output will be written to: {file3}")
    
    # Read and sum file1
    total1 = fileAdd(file1)
    print(f"Sum of {file1}: {total1}")
    
    # Read and sum file2 
    # total2 = fileAdd(file2)
    # print(f"Sum of {file2}: {total2}")
    
    #  Compare sums and merge files 
    # if total1 < total2:
    #     # Write file1 content followed by file2 content to file3
    #     pass
    # else:
    #     # Write file2 content followed by file1 content to file3
    #     pass


if __name__ == "__main__":
    main()


