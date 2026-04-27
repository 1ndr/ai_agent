from functions.get_file_content import get_file_content

#Test Case 1
print('Test Case 1')
print(get_file_content('calculator', 'lorem.txt'))

#Test Case 2
print('Test Case 2')
print(get_file_content('calculator', 'main.py'))

#Test Case 3
print('Test Case 3')
print(get_file_content('calculator', 'pkg/calculator.py'))

#Test Case 4
print('Test Case 4')
print(get_file_content('calculator', '/bin/cat'))

#Test Case 5
print('Test Case 5')
print(get_file_content('calculator', 'pkg/does_not_exist.py'))
