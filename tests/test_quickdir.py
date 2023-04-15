import os
import shutil
import tempfile
import unittest
from quickdir.quickdir import create_directory, remove_directory

class QuickdirTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_create_directory(self):
        dir_name = 'test_dir'
        create_directory(self.test_dir, dir_name)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, dir_name)))

    def test_remove_directory(self):
        dir_name = 'test_dir'
        dir_path = os.path.join(self.test_dir, dir_name)
        os.mkdir(dir_path)
        remove_directory(dir_path)
        self.assertFalse(os.path.exists(dir_path))
