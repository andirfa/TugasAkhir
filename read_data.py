import os
import re

def readData(folder, labels) :
    read_data = []
    read_fileName = []

    dir_path = os.path.dirname(os.path.realpath(__file__))
    corpus_dir = os.path.join(dir_path, folder)

    for i, n in list(enumerate(os.listdir(corpus_dir))):
        with open(os.path.join(corpus_dir, n), mode='r') as f:
            if n.split("_")[0] not in labels :
                labels.append(n.split("_")[0])
                read_data.append([])
                read_fileName.append([])
                # read_label.append(label.index(n.split("_")[0]))

            artikel_doc = f.read()
            i = labels.index(n.split("_")[0])
            # print(n.split("_")[0], i)
            read_data[i].append(re.sub(r"\n"," ",artikel_doc))
            read_fileName[i].append(n)

    max = 0
    for line in read_data :
        if max < len(line) :
            max = len(line)

    data = [] # kalimat setiap file
    labelData = [] # kelas dari setiap file // labels-> nama-nama kelas yang sudah dibaca oleh program
    fileName = [] # nama file
    for i in range(max) :
        for j in range(len(labels)) :
            try :
                data.append(read_data[j][i])
                labelData.append(j)
                fileName.append(read_fileName[j][i])
            except IndexError :
                pass

    return data, labelData, labels, fileName

