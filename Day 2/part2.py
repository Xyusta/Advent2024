def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def increasing(data):
    print("Entered increasing:\n")
    print(f"Data: {data}\n")
    for i in range (len(data) - 1):
        if data[i] > data[i+1] or data[i] == data[i+1] or data[i+1] - data[i] > 3:
            return i
    return -1

def decreasing(data):
    print("Entered decreasing:\n")
    print(f"Data: {data}\n")
    for i in range (len(data) - 1):
        if data[i] < data[i+1] or data[i] == data[i+1] or data[i] - data[i+1] > 3:
            return i
    return -1

def controller(data):
    edge_case = data.copy()
    # Initial Attempt if it works we will have result = -1.
    print("Entered Controller:\n")
    print(f"Data: {data}\n")
    if data[0] < data[1]:
        result = increasing(data)
        if result == -1:
            return 1
        copy = data.copy()
        copy.pop(result)
        data.pop(result + 1)
        if increasing(data) == -1 or decreasing(data) == -1:
            print("Second Try Success\n")
            return 1
        data = copy
        if increasing(data) == -1 or decreasing(data) == -1:
                print("Second Try Success\n")
                return 1
    else:
        if data[0] > data[1]:
            result = decreasing(data)
            if result == -1:
                return 1
            copy = data.copy()
            copy.pop(result)
            data.pop(result + 1)
            if increasing(data) == -1 or decreasing(data) == -1:
                print("Second Try Success\n")
                return 1
            data = copy
            if increasing(data) == -1 or decreasing(data) == -1:
                    print("Second Try Success\n")
                    return 1
    edge_case.pop(0)
    if increasing(edge_case) == -1 or decreasing(edge_case) == -1:
        print("Second Try Success\n")
        return 1
    return 0
    

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    data = read_file(filename)

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
            total_safe += controller(parsed)
        else:
            total_safe += 1
        
    print(f"Total Safe: {total_safe}")
