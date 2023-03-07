import os
filePath = 'C:/Users/User/Documents/PP2/lab6/Z.txt'
# As file at filePath is deleted now, so we should check if file exists or not not before deleting them
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")