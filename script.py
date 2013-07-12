from pyunpack import Archive
# 
import os
import re
import subprocess
cache = '/home/vahid/Workspace/Verilog/cache'
extract = '/home/vahid/Workspace/Verilog/extracts'
result = '/home/vahid/Workspace/Verilog/results'
files_url = []
roots = ''
for root, dirs, files in os.walk(extract):
    # for file in files:
    # ext=os.path.splitext(file)[1]
    # print ext
    # print root
    files_url = files
# print files_url
students_numbers = []
for file in files_url:
    m = re.match(r'.*((90|89|88|87)[0-9]{6}).*', file)
    ns = m.group(1)
    students_numbers.append(ns)



for i in range(len(files_url)):
    Archive(extract +'/'+ files_url[i]).extractall(cache)

    for root, dirs, f in os.walk(cache):

        if f:
            counter = 0
            print f
            print i
            for file in f:
                counter +=1
                ext = os.path.splitext(file)[1]
                print ext
                print root

                if ext == '.v':
                    subprocess.call(['mv',root+'/'+file, result +'/'+ students_numbers[i] +'_'+str(counter)+ext])
                else:
                    subprocess.call(['mv',root+'/'+file, result +'/'+ students_numbers[i] +'_screenshot'+ext])

            subprocess.call(['rm', '-r' ,cache])
            subprocess.call(['mkdir' ,cache])

