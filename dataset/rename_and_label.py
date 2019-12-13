import os
import pandas as pd

df = pd.DataFrame(columns=['image', 'label'])
i = 0
for filename in os.listdir("."):
    if filename.find('.jpg') != -1:
        new_filename = 'image-%03d.jpg' % (i+1)
        os.rename(filename, new_filename  )
        df.loc[i] = [ new_filename, 0 ] 
        i = i + 1


df.to_csv('labels.txt', sep=' ', header=True)

