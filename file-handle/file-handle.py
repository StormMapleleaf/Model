import sys
import os
import re

def remove_empty_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 过滤掉空行
        non_empty_lines = [line for line in lines if line.strip()]

        # 确保输出目录存在
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)

        # 创建输出文件路径
        output_file_path = os.path.join(output_dir, os.path.basename(file_path))

        # 写入非空行到新文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(non_empty_lines)

        print(f"已成功删除空行，并将结果保存到 {output_file_path}。")
    except Exception as e:
        print(f"处理文件时出错: {e}")

def remove_comments(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        #//TODO:存在bug，会删除正则表达式中的符号
        cleaned_lines = []
        for line in lines:
            # 删除 Python 和 Ruby 的行内注释
            cleaned_line = re.sub(r'(?<!["\'])#.*$', '', line)
            # 删除 C/C++、Java、JavaScript 的行内注释
            cleaned_line = re.sub(r'//.*$', '', cleaned_line)
            # 删除多行注释（C/C++、Java、JavaScript）
            cleaned_line = re.sub(r'/{\*.*?\*}/', '', cleaned_line, flags=re.DOTALL)  #TODO:存在bug
           # 删除 PHP 的行内注释
            cleaned_line = re.sub(r'//.*$', '', cleaned_line)
            cleaned_line = re.sub(r'\#.*$', '', cleaned_line) 
            # 删除 HTML 的行内注释
            cleaned_line = re.sub(r'<!--.*?-->', '', cleaned_line, flags=re.DOTALL)
            # 删除 Shell 脚本的行内注释
            cleaned_line = re.sub(r'(?<!["\'])#.*$', '', cleaned_line)

            cleaned_lines.append(cleaned_line)

        # 确保输出目录存在
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)

        # 创建输出文件路径
        output_file_path = os.path.join(output_dir, os.path.basename(file_path))

        # 写入删除注释后的行到新文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(cleaned_lines)

        print(f"已成功删除注释，并将结果保存到 {output_file_path}。")
    except Exception as e:
        print(f"处理文件时出错: {e}")

def remove_empty_comments(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        cleaned_lines = []
        for line in lines:
            cleaned_line = re.sub(r'(?<!["\'])#.*$', '', line)
            cleaned_line = re.sub(r'//.*$', '', cleaned_line)
            cleaned_line = re.sub(r'/{\*.*?\*}/', '', cleaned_line, flags=re.DOTALL)  #TODO:存在bug
            cleaned_line = re.sub(r'//.*$', '', cleaned_line)
            cleaned_line = re.sub(r'\#.*$', '', cleaned_line) 
            cleaned_line = re.sub(r'<!--.*?-->', '', cleaned_line, flags=re.DOTALL)
            cleaned_line = re.sub(r'(?<!["\'])#.*$', '', cleaned_line)
            cleaned_lines.append(cleaned_line)

        non_empty_lines = [line for line in cleaned_lines if line.strip()]
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, os.path.basename(file_path))
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(non_empty_lines)
        print(f"已成功删除空行与注释，并将结果保存到 {output_file_path}。")
    except Exception as e:
        print(f"处理文件时出错: {e}")

if __name__ == "__main__":
    
    if sys.argv[1] == '-rm' and sys.argv[2] == '-empty' and sys.argv[3] == '-comment' or \
       sys.argv[1] == '-rm' and sys.argv[2] == '-comment' and sys.argv[3] == '-empty':
       remove_empty_comments(sys.argv[4])
    elif sys.argv[1] == '-rm' and sys.argv[2] == '-empty':
        remove_empty_lines(sys.argv[3])
    elif sys.argv[1] == '-rm' and sys.argv[2] == '-comment':
        remove_comments(sys.argv[3])
   
    else:
        print("Error")
