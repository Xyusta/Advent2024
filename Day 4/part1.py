import re
import numpy as np

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)


if __name__ == "__main__":
    filename = input("Enter the filename: ")
    data = read_file(filename)

    total = 0

    # Turn data into a 2 dimensional array
    lines = data.splitlines()
    grid = [list(line) for line in lines]

    def search_word(grid, word):
        word_len = len(word)
        total = 0

        # Search horizontally and vertically
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # Horizontal forward
                if j + word_len <= len(grid[i]) and ''.join(grid[i][j:j+word_len]) == word:
                    total += 1
                # Horizontal backward
                if j - word_len >= -1 and ''.join(grid[i][j:j-word_len:-1]) == word:
                    total += 1
                # Vertical down
                if i + word_len <= len(grid) and ''.join(grid[i+k][j] for k in range(word_len)) == word:
                    total += 1
                # Vertical up
                if i - word_len >= -1 and ''.join(grid[i-k][j] for k in range(word_len)) == word:
                    total += 1

        # Search diagonally
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # Diagonal down-right
                if i + word_len <= len(grid) and j + word_len <= len(grid[i]) and ''.join(grid[i+k][j+k] for k in range(word_len)) == word:
                    total += 1
                # Diagonal down-left
                if i + word_len <= len(grid) and j - word_len >= -1 and ''.join(grid[i+k][j-k] for k in range(word_len)) == word:
                    total += 1
                # Diagonal up-right
                if i - word_len >= -1 and j + word_len <= len(grid[i]) and ''.join(grid[i-k][j+k] for k in range(word_len)) == word:
                    total += 1
                # Diagonal up-left
                if i - word_len >= -1 and j - word_len >= -1 and ''.join(grid[i-k][j-k] for k in range(word_len)) == word:
                    total += 1

        return total

    total = search_word(grid, "XMAS")



    print(total)