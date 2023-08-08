import re
import py2exe
import hashlib

def transcode(file, encry):
    res = ""
    txt = read_file(file)
    find_code = r'//(.*)'
    lines = txt.split('\n')
    for line in lines:
        match = re.search(find_code, line)
        if match:
            res_txt = match.group(1)
            if encry:
                encrypted_txt = encryption(res_txt)
                encrypted_line = line.replace(res_txt, encrypted_txt, 1)
                res += encrypted_line + '\n'
            else:
                decrypted_txt = decryption(res_txt)
                decrypted_line = line.replace(res_txt, decrypted_txt, 1)
                res += decrypted_line + '\n'
        else:
            res += line + '\n'
    f = open(file, 'w+')
    f.write(res)




def read_file(file):
    with open(file, encoding='UTF-8') as f:
        read_all = f.read()
        f.close()

    return read_all



def encryption (line):
    return line[::-1]

def decryption (line):
    return line[::-1]
    

def getfile():
    file = input('Please input the file name:')
    return file



if __name__ == '__main__':
    file = getfile()
    encry = input('Please input 1 for encryption, 0 for decryption:')
    print(file)
    transcode(file, encry)
