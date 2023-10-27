import calendar
import os

yy = 2017
print(calendar.calendar(int(yy)))

cwd = os.getcwd()
print("Current working directory:", cwd)

file_name = "your_file_name_here"  # Replace 'your_file_name_here' with the actual file name
result = os.path.exists(file_name)
print("Does the file exist?", result)
