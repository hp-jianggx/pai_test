import os
import os.path

max_depth = 2
def dfs_showdir(path, depth):
    if depth == max_depth:
        return
    for item in os.listdir(path):
            print("| " * depth + "+--" + item)
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                try:
                    dfs_showdir(newitem, depth + 1)
                except:
                    pass

print('/')
dfs_showdir('/', 0)
