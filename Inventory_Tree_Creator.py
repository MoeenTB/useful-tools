import os
import pathlib

def name_stripper(name: str, verbose: bool):
    bgn = 1900
    fin = 2023
    found_year = False
    dc = name.count('.')
    uc = name.count('_')
    sc = name.count(' ')
    if (dc > uc) and (dc > sc):
        seperator = '.'
    elif (uc > dc) and (uc > sc):
        seperator = '_'
    else:
        seperator = ' '
    name_l = name.split(seperator)
    if verbose:
        print(name_l)
    for i, exp in enumerate(name_l[1:]):
        if exp.startswith('('):
            closing_ind = exp.find(')')
            t = exp[1:closing_ind]
        else:
            t = exp
        if verbose:
            print(t)
        try:
            t_i = int(t)
        except:
            continue
        if bgn <= t_i <= fin:
            name_new = ' '.join(name_l[:1+i])
            found_year = True
            break
    if not found_year:
        name_new = ' '.join(name_l)
    return name_new

def tree_creator(directory, depth, the_list):
    # root_l = os.listdir(directory)
    dir_s = str(directory)
    files = [file_d for file_d in directory.iterdir() if file_d.is_file()]
    files.sort()
    for f in files:
        s = str(f)
        s = s.replace(dir_s + "\\", "    "*depth + "|_ ")
        # print(s)
        the_list.append(s+'\n')
    sub_dirs = [sub_dir for sub_dir in directory.iterdir() if sub_dir.is_dir()]
    sub_dirs.sort()
    for sub_dir in sub_dirs:
        s = str(sub_dir)
        s = s.replace(dir_s + "\\", "    "*depth + "|_ ")
        # print(s)
        the_list.append(s+'\n')
        tree_creator(sub_dir, depth+1, the_list)


print("Initiating Preprocess")

source_dir = r"D:\"
output_dir = r"D:\"
output_name = "Sample"

source = pathlib.Path(source_dir)
the_lines = [str(source) + '\n']
tree_creator(source, 1, the_lines)
# print(the_lines)

# names = []
# source_l = os.listdir(source_dir)
# for name in source_l:
#     names.append(name_stripper(name, False)+'\n')
# names.sort()
with open(os.path.join(output_dir, output_name), 'w', encoding='utf-8') as f:
    f.writelines(the_lines)

print("Done!")
