#coding=utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
import sys

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    corpus = list()
    data = dict()
    with open(input_file, 'r') as fin:
        for line in fin.readlines():
            try:
                info = line.strip().split('\t')
                date = info[1].split('-')[0]
                content = ' '.join(info[3:])
                corpus.append(content)
                if date in data:
                    data[date].append(content)
                else:
                    data[date] = list()
                    data[date].append(content)
            except:
                print("Bad line[%s]"%line.strip())
                continue
    tfidf_vec = TfidfVectorizer(max_df=0.3, min_df=3)
    tfidf_vec.fit(corpus)
    wordlist = tfidf_vec.get_feature_names()
    print("total words[%d]" %len(wordlist))

    num_line = 0
    with open(output_file, 'w') as fout:
        with open(input_file, 'r') as fin:
            for line in fin.readlines():
                num_line += 1
                if num_line%500 == 0:
                    print("process[%d]" %num_line)
                try:
                    info = line.strip().split('\t')
                    content = ' '.join(info[3:])
                except:
                    continue
                tfidf = tfidf_vec.transform([content])
                tfidf = tfidf.toarray()
                keywords = list()
                for i in range(len(tfidf[0])):
                    if tfidf[0][i] > 0:
                        keywords.append((wordlist[i], tfidf[0][i]))
                keywords = sorted(keywords, key=lambda x:x[1], reverse=True)
                keywords = keywords[:5]
                if num_line == 5:
                    print(keywords)
                keywords = [x[0] for x in keywords]
                fout.write(line.strip()+'\t'+'|'.join(keywords)+'\n')
