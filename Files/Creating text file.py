import os
file_path = r'C:\...'
if os.path.exists(file_path):
    print('exists')
else:
    with open(file_path, 'w+t') as fp:
        fp.write('first line')
        