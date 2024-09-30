import os
import sys
import subprocess

def convert_mkv_to_mp4(input_file):
    output_dir = './out'
    os.makedirs(output_dir, exist_ok=True)  # 创建输出目录（如果不存在）

    # 获取输出文件名
    output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_file))[0]}.mp4")

    # 使用ffmpeg命令进行转换
    command = ['ffmpeg', '-i', input_file, '-codec', 'copy', output_file]
    subprocess.run(command)

    print(f"转换完成: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python convert.py 输入文件.mkv")
        sys.exit(1)

    input_file = sys.argv[1]
    convert_mkv_to_mp4(input_file)
