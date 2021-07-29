from RecursivePathsToList import GetPaths
from os import environ as env
from sys import argv
import shutil
import json
import os

META_FILE = env.get("META_FILE")
if type(META_FILE) != str:
    META_FILE = "meta.json"

# Load json into variable
with open(META_FILE, 'r') as f:
    meta = json.loads(f.read())

for domain in meta:
    # Translate enviroment variables into real paths and replace them
    # As of right now, the format does not support character escaping (\$)
    realdir:str = meta[domain]["real_dir"]
    while realdir.count('$') > 0:
        starti = realdir.index('$')
        if realdir.count('/', starti) > 0:
            endi = realdir.index('/',starti)
        else: endi = realdir.__len__()
        #TODO: Expand to check if variable is a list (/path/one:/path/two:etc..), if so, select first
        env_variable = env.get(realdir[starti+1:endi])
        realdir = realdir.replace(realdir[starti:endi], env_variable, 1).replace("//",'/')
    meta[domain]["real_dir"] = realdir
    
    # Fetch every file path from under a domain and generate a list of paths relative to the domain
    #TODO: Define argument and/or env variable to specify domains location (something like ~/.local/share/domains/...)
    domain_full_path = os.getcwd()+'/'+domain
    meta[domain]["files"] = GetPaths(domain_full_path)
    meta[domain]["files"].insert(0, domain_full_path)
    for path in meta[domain]["files"]:
        real_path = path.replace(domain_full_path,meta[domain]["real_dir"], 1).replace("//",'/')
        if os.path.isdir(path) and not os.path.isdir(real_path):
            os.makedirs(real_path)
        elif os.path.isfile(path):
            shutil.copy(path,real_path)
        
        print(path,"=>",real_path)
