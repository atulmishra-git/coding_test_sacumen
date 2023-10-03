import os
import glob
import multiprocessing

import boto3
from google.cloud import storage

from .config import (
    DIR_PATH, 
    FILES_TO_GOOGLE, 
    FILES_TO_AWS, 
    S3_BUCKET,
    GCLOUD_BUCKET,
    USE_THREAD
)

"""
This package use simple thread method to demonstrate file upload
"""

def read_dir():
    print(f"Reading root directory {DIR_PATH}")

    """
    Read files everywhere and return the files to upload to google and aws
    """
    google_files = []
    aws_files = []
    for filename in glob.iglob(DIR_PATH + '**/**', recursive=True):
        for gfile in FILES_TO_GOOGLE:
            if os.path.basename(filename).endswith(f'.{gfile}'):
                google_files.append(filename)
        
        for afile in FILES_TO_AWS:
            if os.path.basename(filename).endswith(f'.{afile}'):
                aws_files.append(filename)
    return google_files, aws_files


def upload_to_s3(files):
    try:
        s3 = boto3.resource('s3')
        for file in files:
            s3.Bucket(S3_BUCKET).upload_file(file, os.path.basename(file))
        return True
    except Exception:
        return False


def upload_to_gcs(files):
    credentials_file = "path/to/your/credentials.json"
    try:
        storage_client = storage.Client.from_service_account_json(credentials_file)
        bucket = storage_client.bucket(GCLOUD_BUCKET)
        for file in files:
            blob = bucket.blob(os.path.basename(file))
            blob.upload_from_filename(file)
        return True
    except Exception:
        return False


def run():
    google_files, aws_files = read_dir()

    print("Files to Upload to Google ", google_files)
    print("Files to Upload to AWS ", aws_files)

    if google_files:
        if USE_THREAD:
            t1 = multiprocessing.Process(target=upload_to_gcs, args=google_files)
            t1.start()
        else:
            if upload_to_gcs(google_files):
                print("Files Uploaded to Google")
                return True
    
    if aws_files:
        if USE_THREAD:
            t2 = multiprocessing.Process(target=upload_to_s3, args=aws_files)
            t2.start()
        else:
            if upload_to_s3(aws_files):
                print("Files Uploaded to s3")
                return True
    return

