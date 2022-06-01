from pathlib import Path

parent = Path(__file__).parents[2]
#file_path = curr_dir.joinpath('data/otherfile.txt')
#print(file_path)

#path = parent / 'data' / 'FR' 
path = parent.joinpath('data','FR')
print(path)