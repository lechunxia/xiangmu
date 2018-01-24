import unittest

if __name__ == '__main__':
     test_case = unittest.defaultTestLoader.discover(".", pattern='*Test.py')
     unittest.TextTestRunner().run(test_case)
