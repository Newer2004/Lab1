import os
path = r'C:/Users/User/Documents/PP2/lab6'
print(os.path.exists(path))
path = r'C:/Users/User/Documents/PP2/lab7'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))