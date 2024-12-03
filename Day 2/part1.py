def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def increasing(data):
    print("Entered increasing:\n")
    print(f"Data: {data}\n")
    for i in range (len(data) - 1):
        if data[i] > data[i+1] or data[i] == data[i+1] or data[i+1] - data[i] > 3:
            print("False\n")
            return 0
    print("True\n")
    return 1

def decreasing(data):
    print("Entered decreasing:\n")
    print(f"Data: {data}\n")
    for i in range (len(data) - 1):
        if data[i] < data[i+1] or data[i] == data[i+1] or data[i] - data[i+1] > 3:
            print("False\n")
            return 0
    print("True\n")
    return 1

if __name__ == "__main__":
    data = read_file('data.txt')

    parsed = []
    total_safe = 0

    lines = data.split('\n')
    for line in lines:
        parsed.clear()
        numbers = line.split()
        if len(numbers) == 0:
            continue
        for i in range (len(numbers)):
            parsed.append(int(numbers[i]))
        #print(f"Parsed: {parsed}\n")
        if (len(parsed) > 1):
            if parsed[0] < parsed[1]:
                total_safe += increasing(parsed)
            if (parsed[0] > parsed[1]):
                total_safe += decreasing(parsed)
        else:
            total_safe += 1
        
    print(f"Total Safe: {total_safe}")
