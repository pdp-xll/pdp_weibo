#coding=utf-8
import jieba
import re
import sys

def normalize(line):
    chinese_pattern = re.compile('[^\u4e00-\u9fa5a-zA-Z0-9\\.]')
    line = re.sub(chinese_pattern, " ", line)
    dot_pattern = re.compile('\\.\\.+')
    line = re.sub(dot_pattern, " ", line)
    white_space_pattern = re.compile('\\s+')
    line = re.sub(white_space_pattern, " ", line)
    line = line.lower()
    return line.strip()

def seg(line):
    seg_line = ' '.join(jieba.cut(line))
    return normalize(seg_line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(output_file, 'w') as fout:
        with open(input_file, 'r') as fin:
            for line in fin.readlines():
                line_info = line.strip().split('\t')
                try:
                    line_info[3] = seg(line_info[3])
                    if line_info[0] == "repost":
                        line_info[4] = seg(line_info[4])
                    fout.write('\t'.join(line_info)+'\n')
                except:
                    print("Error line[%s]"%line.strip())
