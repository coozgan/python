import re
import os

directory = input('What is the Directory: ')
directory = directory.replace('\\', '')
number_pattern = input('what is the number pattern: ')
remove_pattern = input('What should I remove from the pattern?: ')
number_pattern = re.compile(number_pattern)
series_title = input("Series Title: ")
series_file = input('What is the Episodes File name: ')
file_open = open(series_file, "r")
episodes = file_open.read().split('\n')
episodes.insert(0, '')
print(episodes)
os.chdir(directory)
for files in os.listdir():
    matches = number_pattern.finditer(files)
    for match in matches:
        file_type = files.split('.').pop()
        number = int(match[0].replace(remove_pattern,''))
        file_name = f"{series_title} EP{number:02d} - {episodes[number]}.{file_type}"
        print(file_name)
        os.rename(files, file_name)

