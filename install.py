import pandas as pd
import os
from subprocess import Popen, PIPE, STDOUT


def exe_command(command):
    """
    执行 shell 命令并实时打印输出
    :param command: shell 命令
    :return: process, exitcode
    """
    print(command)
    process = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True)
    with process.stdout:
        for line in iter(process.stdout.readline, b''):
            print(line.decode().strip())
    exitcode = process.wait()
    return process, exitcode


projects = ['bcel', 'codec', 'collections', 'configuration', 'dbcp', 'digester', 'fileupload', 'net', 'pool']

# urls_set = set()
# for project_name in projects:
#     print('Installing project:'+project_name)
#     csv_file_path = '/Users/sunchen/data/all_label_data/'+project_name+'.csv'
#     csv_data = pd.read_csv(csv_file_path)
#     for index, row in csv_data.iterrows():
#         if index > 1:
#             urls_set.add(row['buggy commit'])
#     for url in urls_set:
#         print('Installing commit ID:'+url)
#         file_path = '/Users/sunchen/data/commons-'+project_name+'/commons-'+project_name+'-'+url+'/'
#         target_file_path = file_path + 'target/'
#         if os.path.exists(target_file_path):
#             continue
#         # file_path = '/Users/sunchen/data/maven-dependency-plugin/maven-dependency-plugin-' + url + '/'
#         cmd = 'source ~/.bash_profile && cd ' + file_path + '&&' + 'mvn install'
#         exe_command(cmd)
#     urls_set.clear()

for project_name in projects:
    print('Installing project:' + project_name)
    file_path = '/Users/sunchen/data/warning-inducing context/warning slicing/' + project_name + '_commits.txt'
    file = open(file_path, 'r')
    str = file.read()
    commit_id_list = str.split(',')
    for commit_id in commit_id_list:
        if commit_id == '':
            continue
        commit_path = '/Users/sunchen/data/commons-' + project_name + '/commons-' + project_name + '-' + commit_id + '/'
        cmd = 'source ~/.bash_profile && cd ' + commit_path + '&&' + 'mvn install'
        exe_command(cmd)

