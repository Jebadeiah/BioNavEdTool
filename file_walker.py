from os import path
from pathlib import Path


def term_in_file(term, file):
    with open(file, 'r') as fp:
        contents = fp.read()
        if term in contents:
            return True


def file_walker(file_path, search_term): 
    i = Path(file_path)
    for p in i.glob('**/*'):
        split_page = path.splitext(p)
        if split_page[1].lower() != '.html':
            print("Not a web page!")
            print(split_page)
            continue
        else:
            print("Web page!")
            if term_in_file(search_term, p):
                return p
