from os import chdir, path, walk

from term_in_file import  term_in_file


def walker(root_mother, search_term):
    pages = []
    chdir(root_mother)
    for root_child, dirs, files in walk('.'):
        for page in files:
            split_page = path.splitext(page)
            if split_page[1].lower() != '.html':
                continue
            else:
                if term_in_file(search_term, page):
                    return page
