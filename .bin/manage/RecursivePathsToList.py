from os import listdir as listDirectory
from os.path import isdir as isDir

def GetPaths(parent_dir:str) -> list:
    return_list = []
    for f in listDirectory(parent_dir):
        full_path = parent_dir+'/'+f
        if isDir(full_path):
            return_list.append(full_path)
            for subfile in GetPaths(full_path):
                return_list.append(subfile)
        else:
            return_list.append(full_path)
    return return_list
