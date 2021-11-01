import unittest

from pathlib import Path

from file_walker import file_walker, term_in_file

class file_walker_tests(unittest.TestCase):

    def test_term_in_file(self):
        file_path = Path("test assets/file_walker assests/test_folder/webpage1.html")
        file_path2 = Path("test assets/file_walker assests/test_folder/test_subfolder/webpage2.html")
        search_term = '<div id="container">'
        output = term_in_file(file_path, search_term)
        output2 = term_in_file(file_path2, search_term)

        self.assertEqual(output, True)
        self.assertEqual(output2, False)

    def test_upper(self):
        file_path = Path("test assets/file_walker assests/test_folder")
        search_term = '<div id="container">'
        desired_output = {
            True: "webpage1.html", 
            False: "test_subfolder/webpage2.html"}
        output = file_walker(file_path, search_term)

        self.assertEqual(output, desired_output)

if __num__ == '__main__':
    unittest.main()