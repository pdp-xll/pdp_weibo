#coding=utf-8
import sys

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    year_keywords = dict()
    with open(input_file, 'r') as fin:
        for line in fin.readlines():
            info = line.strip().split('\t')
            try:
                date = info[1].split('-')[0]
                if date not in year_keywords:
                    year_keywords[date] = dict()
                keywords = info[-1].split('|')
            except:
                continue
            for keyword in keywords:
                if keyword in year_keywords[date]:
                    year_keywords[date][keyword] += 1
                else:
                    year_keywords[date][keyword] = 1

    top_year_keywords = dict()
    for year, keywords in year_keywords.items():
        keywords = sorted(keywords.items(), key = lambda x:x[1], reverse=True)
        keywords = keywords[:50]
        keywords = [x[0] for x in keywords]
        top_year_keywords[year] = keywords

    with open(output_file, 'w') as fout:
        for year, keywords in top_year_keywords.items():
            fout.write(year+'\t'+' '.join(keywords)+'\n')
