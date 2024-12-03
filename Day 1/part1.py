def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    data = read_file('data.txt')

    left = []
    right = []

    lines = data.split('\n')
    for line in lines:
        numbers = line.split()
        if len(numbers) == 0:
            continue
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

    left.sort()
    right.sort()

    total_dif = 0
    for i in range(len(left)):
        total_dif += abs(left[i] - right[i])

    print(f"Total Difference: {total_dif}")