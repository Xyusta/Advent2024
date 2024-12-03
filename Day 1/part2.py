from collections import defaultdict

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

if __name__ == "__main__":
    data = read_file('data.txt')

    left = defaultdict(int)
    right = defaultdict(int)

    lines = data.split('\n')
    for line in lines:
        numbers = line.split()
        if len(numbers) == 0:
            continue
        left[int(numbers[0])] += 1
        right[int(numbers[1])] += 1

    product_sum = 0
    for key in left:
        product_sum += key * right[key]

    print(f"Product sum: {product_sum}")