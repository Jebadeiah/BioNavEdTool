from code_indexes import code_indexes


def code_injector(file_path, code_location, injection):
    if not code_indexes(file_path, code_location):
        raise ValueError
    else:
        list_of_indexes = code_indexes(file_path, code_location)
        proceed = input(f"We found {list_of_indexes.length()} instances of that code. Would you like to proceed with code injection?\n")
        if proceed:
            fp = open(file_path, "r")
            contents = fp.readlines()
            fp.close()

            for index in list_of_indexes:
                print(contents[index, index + 1, index + 2])
                cont = input("Would you like to inject your code acter the first line?")
                if cont:
                    contents.insert(index, injection)

                    fp = open(file_path, "w")
                    contents = "".join(contents)
                    fp.write(contents)
                    fp.close()