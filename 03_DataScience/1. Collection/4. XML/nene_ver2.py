import os
import re
dir_name="V2_BigData"
dir_delimeter='\\'
nene_dir="Nene_Data"
nene_file='nene'
csv='csv'
record_limit=3
# if not os.path.isdir(os.path.join(os.getcwd(),dir_name)) :
#     os.mkdir(os.path.join(os.getcwd(),dir_name))
#     os.mkdir(os.path.join(os.getcwd()+dir_name,nene_dir))
#
if not os.path.exists('.'+dir_delimeter+dir_name) :
    os.mkdir('.'+dir_delimeter+dir_name)
    os.mkdir('.'+dir_delimeter+dir_name+dir_delimeter+nene_dir+'1')
#
# print(os.getcwd())
