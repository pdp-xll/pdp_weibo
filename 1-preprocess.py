#coding=utf-8
import sys
import re

def clean_data(line):
    pattern = re.compile('<.*?>')
    return re.sub(pattern, " ", line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(output_file, 'w') as fout:
        with open(input_file, 'r') as fin:
            for line in fin.readlines():
                line = line.strip().split('\t')
                #repost_flag = True if line[0]=='repost' else False
                repost_flag = line[0] 
                create_time = line[1]
                if len(create_time.split('-'))==2:
                    create_time = "2019-"+create_time
                page_num = line[2]
                post = clean_data(line[3])
                if repost_flag == "repost":
                    retweeted = clean_data(line[4])
                else:
                    retweeted = ""
                fout.write(repost_flag+'\t'+create_time+'\t'+page_num+'\t'+post+'\t'+retweeted+'\n')
