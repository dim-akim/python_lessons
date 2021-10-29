with open('dataset_24465_4.txt', 'r') as file1, open('answer.txt', 'w') as file2:
    lines = [line for line in file1]
    lines = lines[::-1]
    file2.write(''.join(lines))
