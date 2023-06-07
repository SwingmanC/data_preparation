import os.path

import requests
import xlrd
import csv
import pandas as pd
from zipfile import ZipFile

# projects = ['bcel', 'codec', 'collections', 'configuration', 'dbcp', 'digester', 'fileupload', 'net', 'pool']
projects = ['mavendp']


def download_file(url, file_pname, chunk_size=1024*4):
    """
    url: file url
    file_pname: file save path
    chunk_size: chunk size
    """
    response_data_file = requests.get(url, stream=True)
    with open(file_pname, 'wb') as f:
        for chunk in response_data_file.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)


urls_set = set()
for project_name in projects:
    print('Downloading project:'+project_name)
    csv_file_path = '/Users/sunchen/data/all_label_data/'+project_name+'.csv'
    csv_data = pd.read_csv(csv_file_path)
    for index, row in csv_data.iterrows():
        if index > 1:
            urls_set.add(row['buggy commit'])
    for url in urls_set:
        print('Downloading commit ID:'+url)
        # file_save_path = '/Users/sunchen/data/commons-'+project_name+'/'
        file_save_path = '/Users/sunchen/data/maven-dependency-plugin/'
        if os.path.exists(file_save_path) is False:
            os.mkdir(file_save_path)
        # file_path = '/Users/sunchen/data/commons-'+project_name+'/commons-'+project_name+'-'+url+'/'
        file_path = '/Users/sunchen/data/maven-dependency-plugin/maven-dependency-plugin-' + url + '/'
        if os.path.exists(file_path) is False:
            # download_file('https://github.com/apache/commons-' + project_name + '/archive/' + url + '.zip',
            #               file_save_path + url + '.zip')
            download_file('https://github.com/apache/maven-dependency-plugin/archive/' + url + '.zip',
                          file_save_path + url + '.zip')
            file = ZipFile(file_save_path + url + '.zip')
            file.extractall(file_save_path)
            file.close()
            os.remove(file_save_path + url + '.zip')
    urls_set.clear()

# excel_data = xlrd.open_workbook('/Users/sunchen/Downloads/mark.xlsx')
# for i in range(5, 6):
#     sheet = excel_data.sheet_by_index(i)
#     project_name = sheet.cell_value(1, 4)
#     file_save_path = '/Users/sunchen/data/'+project_name+'/'
#     if os.path.exists(file_save_path) is False:
#         os.mkdir(file_save_path)
#     for cell in sheet.col(6):
#         if cell.value != 'buggy commit':
#             urls_set.add(cell.value)
#     for url in urls_set:
#         print('Downloading commit ID:'+url)
#         download_file('https://github.com/apache/'+project_name+'/archive/'+url+'.zip', file_save_path+url+'.zip')
#         file = ZipFile(file_save_path+url+'.zip')
#         file.extractall(file_save_path)
#         file.close()
#         os.remove(file_save_path+url+'.zip')
#     urls_set.clear()