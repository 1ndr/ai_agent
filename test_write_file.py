import unittest
from functions.write_file import write_file

#Test Case 1
print("Test Case 1")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

#Test Case 2
print("Test Case 2")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

#Test Case 3
print("Test Case 3")
print(write_file("calculator", "/temp/temp.txt", "this should not be allowed"))
