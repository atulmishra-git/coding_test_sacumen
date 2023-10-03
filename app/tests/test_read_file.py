import unittest
from ..read_file import read_dir, upload_to_gcs, upload_to_s3


class TestReadFile(unittest.TestCase):
    def test_read_dir_google_files(self):
        google_files, _ = read_dir()
        self.assertNotEqual([], google_files)
    
    def test_read_dir_google_files_empty(self):
        google_files, _ = read_dir()
        self.assertEqual([], google_files)
    
    def test_read_dir_s3_files(self):
        _, aws_files = read_dir()
        self.assertNotEqual([], aws_files)
    
    def test_read_dir_s3_files_empty(self):
        _, aws_files = read_dir()
        self.assertEqual([], aws_files)
    
    def test_upload_to_gcs_ok(self):
        google_files, _ = read_dir()
        ok = upload_to_gcs(google_files)
        self.assertTrue(ok)
    
    def test_upload_to_s3_ok(self):
        _, aws_files = read_dir()
        ok = upload_to_s3(aws_files)
        self.assertTrue(ok)
    
    def test_upload_to_gcs_failed(self):
        google_files, _ = read_dir()
        ok = upload_to_gcs(google_files)
        self.assertFalse(ok)
    
    def test_upload_to_s3_failed(self):
        _, aws_files = read_dir()
        ok = upload_to_s3(aws_files)
        self.assertFalse(ok)
