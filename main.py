from pathlib import Path

from code_injector import code_injector
from file_walker import file_walker


# programs to write:
# if_term_in_file
# inject_code
# css_duplicate_check

root_directory = Path('.')
injection = """\
    <div>
        <button>Blue</button>
    </div>"""

# Test name - Bionavedtool. 
##########################################################################################################################################################
#
# Below are functions I need to write#
#
##########################################################################################################################################################
#<
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
# addon 4. We can choose to open a program called tree_planter, where you start with a single empty text field and a '+' button. Pressing the + button 
# adds more text fields in that row. Putting text in the text field causes a new, empty text field to appear below it in a tree. Once you've built out
# the whole directory tree, press a button to create that IRL at the location indicated in another text field labelled 'root'. 
#
##########################################################################################################################################################

search_term = input("Input the code we're searching for: \n")
for file in file_walker(root_directory, ""):
    code_injector(injection, Path(file))