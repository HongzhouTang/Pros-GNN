import numpy as np
import os

files = os.listdir('file_path')  #the file path is  mutation_pdb with no processing

for file in files:
    file_name=file[:5]
    with open('no_preprocessing_mutation/'+file, 'r') as f:
        data = f.read().strip().split('\n') 
        with open('mutation_pdb/'+file+'_mutation.pdb',"w") as f:
            for a in data:
                if a[:4] == 'ATOM':
                    b = a[23:26]
                    b = int(b)
                    c = file[7:-13]
                    c = int(c)
                    if c-1 <= b <= c+1:                        
                         f.write(a+'\n')