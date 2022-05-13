#test
import numpy as np

list_1 = [np.nan]
list_2 = ['hey', 'hello']

concat = [*list_1,*list_2]
print(concat)