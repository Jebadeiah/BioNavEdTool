def code_indexes(file_path, code, after = True):
    file_contents = open(file_path, 'r')
    ret = []

    for i, line in enumerate(file_contents.readlines()):
        if code in line:
            if after:
                ret.append(i + 1)
            else:
                ret.append(i)
    file_contents.close()
    
    return ret
