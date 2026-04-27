from functions.get_files_info import get_files_info

#Test Case 1
print("Results for current directory:")
print(get_files_info('calculator', '.'))

#Test Case 2
print("Results for \'pkg\' directory:")
print(get_files_info('calculator', 'pkg'))

#Test Case 3
print("Results for '/bin' directory:")
print(get_files_info('calculator', '/bin/'))

#Test Case 4
print("Results for '../' directory:")
print(get_files_info('calculator', '../'))

