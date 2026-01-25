try:
    count=1
    with open('sample.txt') as fh:
        while True:
            line = fh.readline()
            if(line == ''):
                break
            print(f"Line {count}: {line}")
            count+=1
except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found")

