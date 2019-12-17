import os
import pandas as pd
import random

df = pd.DataFrame(columns=['image', 'label'])
classes = ['Jeng-Wu','Chu-Wu']
df_classes = pd.DataFrame({'class':classes})
i = 0
for filename in os.listdir("."):
    if filename.find('.jpg') != -1:
        new_filename = 'image-%03d.jpg' % (i+1)
        os.rename(filename, new_filename  )
        label = classes[random.randint(0,len(df_classes)-1)]
        df.loc[i] = [ new_filename, label ] 
        i = i + 1


df.to_csv('labels.txt', sep=' ', header=True, index=False)
df_classes.to_csv('classes.txt', sep=' ', header=True, index=False)

