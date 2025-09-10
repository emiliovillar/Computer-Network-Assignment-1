import sys

def fileAdd(filename):
    #reads text file, converts to a list of numbers, returns sum
    numbers = []
    content = [] # Jay added this to keep original for later

    #open file
    with open(filename, 'r') as f:
        for line in f:
            #Store the original line
            content.append(line)
            #strip whitespace and convert
            line = line.strip()
            if line: # skip empty line
                try:
                    numbers.append(float(line))
                except ValueError:
                    print(f"Warning: Skipping non numeric value '{line}' in {filename}")
        
        total = sum(numbers)
        return total, content #jay added content 
    

def writeFiles(output_file, content1, content2):
    """Write the contents of two files to the output file"""
    with open(output_file, 'w') as f:
        # Write first content
        for line in content1:
            f.write(line)
        # Write second content
        for line in content2:
            f.write(line)

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
    total1, content1 = fileAdd(file1)
    print(f"Sum of {file1}: {total1}")
    
    # Read and sum file2 
    total2, content2 = fileAdd(file2)
    print(f"Sum of {file2}: {total2}")

    # Compare sums and merge files 
    if total1 < total2:
        # Write file1 content followed by file2 content to file3
        print(f"Writing {file1} first (smaller sum: {total1}), then {file2}")
        writeFiles(file3, content1, content2)
    else:
        # Write file2 content followed by file1 content to file3
        print(f"Writing {file2} first (smaller or equal sum: {total2}), then {file1}")
        writeFiles(file3, content2, content1)
    
    print(f"Successfully wrote merged content to {file3}")


if __name__ == "__main__":
    main()


