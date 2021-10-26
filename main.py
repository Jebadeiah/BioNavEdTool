import os


root_directory = ""

# Test name - Bionavedtool. 
##########################################################################################################################################################
#
# Below are functions I need to write#
#
##########################################################################################################################################################
#
# 1. Function to scrub for files with a specific extension and store their locations in a... dicitonary? Some sort of key, val data structure. I don't yet
# know how many dimensions...
#
# 2. If we choose html, we want to take a string of characters and search each page in our dictionary for that string. If the code is not there, provide 
# the user with the option to add that string as code in the page. I would also like to see the initial code side-by-side with the proposed new code.
#
# 3. If we choose CSS, search the code for duplicate classes. If we find duplicate code, we want to check our HTML for those classes, as well, and store 
# those in a separate dictionary. We'll then be given the option to rename the class and refactor the code in all HTML that previously used that class to
# the new name. 
#
##########################################################################################################################################################


def search(root_mother):

    os.chdir(root_mother)
    for root_child, dirs, files in os.walk('.'):
        for page in files:
            print(page)
        print("\n--------- Those were the web pages. Now, to the directories. ---------\n")
        for folder in dirs:
            print(folder)
        print("\n----------------------- Now back to the files! -----------------------\n")

test_directory = "../../BIOS Navigator"

search(test_directory)
