############# to create folders ############
import os
folders = ['Processing','Processed','Queue']
try:
    for folder in folders:
        path = os.path.join('',folder)
        os.mkdir(path)
except OSError as error: 
    print(error)