import os


result = []
for current_dir, dirs, files in os.walk('main'):
    for file in files:
        if '.py' in file:
            result.append(current_dir)
            break

result.sort()

with open('main_ans.txt', 'w') as file:
    content = '\n'.join(result)
    file.write(content)
