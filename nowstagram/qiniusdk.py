# -*- encoding=UTF-8 -*-

from nowstagram import app
from qiniu import Auth,put_stream,put_file,put_data
import os

print app.config['ACCESS_KEY']
access_key = app.config['ACCESS_KEY']
secret_key = app.config['SECRET_KEY']
q = Auth(access_key, secret_key)

bucket_name=app.config['BUCKET_NAME']
domain_prefix = app.config['QINIU_DOMAIN']

def qiniu_upload_file(source_file,save_file_name):
    token = q.upload_token(bucket_name, save_file_name,3600)
    # source_file.save(os.path.join(save_dir, save_filename))
    ret, info = put_data(token, save_file_name, source_file.stream)
    # ret, info = put_stream(token, save_filename,source_file.stream,"qiniu",os.fstat(source_file.stream.fileno()))
    # ret, info = put_stream(token, save_filename, source_file.stream, "qiniu", os.fstat(source_file.stream.tell()))
    print type(info.status_code), info
    if info.status_code == 200:
        return domain_prefix + save_file_name
    return None
