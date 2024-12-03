import re

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    data = read_file(filename)

    while "don't()" in data:
        start = data.find("don't()")
        stop = data.find("do()", start)
        
        # If no closing do() is found, remove everything after "don't()"
        if stop == -1:
            data = data[:start]
            break
    
        # Remove "don't()" and the content up to and including the closing ")"
        data = data[:start] + data[stop + 1:]

    total = 0
    match = r"mul\(\d{1,3},\d{1,3}\)"

    for m in re.finditer(match, data):
        numbers = re.findall(r'\d{1,3}', m.group())
        if numbers:
            total += int(numbers[0]) * int(numbers[1])
            
    print(total)