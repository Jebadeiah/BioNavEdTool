import codecs


def term_in_file(term, file):
    with open(file, 'r') as fp:
        contents = fp.read()
        if term in contents:
            return True
