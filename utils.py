import os

person2id = {}

with open('p2id.tsv','r') as f:
    for line in f:
        p, i = line[:-1].split('\t')
        person2id[p] = i

def prof_list():
    D = {}
    with open('list.tsv','r') as f:
        for line in f:
            line = line.split()
            if len(line) == 2:
                mn, fn = line
                D[mn] = fn

    return D


def get_entities():
    D = {}
    path = '%s/%s'%('entities','masculine')
    for fname in os.listdir(path):
        prof = fname.split('.')[0]
        D[prof] = {}
        with open('%s/%s'%(path,fname)) as f:
            for line in f:
                if len(line) > 2:
                    name, year, val = line.split('\t')
                    if not year in D[prof]:
                        D[prof][year] = {}
                    D[prof][year][name] = int(float(val[:-1]))

    D2 = {}

    path = '%s/%s'%('entities','feminine')
    for fname in os.listdir(path):
        prof = fname.split('.')[0]
        D2[prof] = {}
        with open('%s/%s'%(path,fname)) as f:
            for line in f:
                if len(line) > 2:
                    name, year, val = line.split('\t')
                    if not year in D2[prof]:
                        D2[prof][year] = {}
                    D2[prof][year][name] = int(float(val[:-1]))

    return D,D2


def get_title_freq():
    D = {}
    fnames = sorted(os.listdir('masculine'))
    for j,y in enumerate(fnames):
        with open('masculine/%s'%y,'r') as f:
            for line in f:
                job,_,_,fr = line.split()
                fr = float(fr)
                if not job in D:
                    D[job] = [[yr.split('.')[0],0.] for yr in fnames]
                D[job][j][1] = fr

    D2 = {}
    fnames = sorted(os.listdir('feminine'))
    for j,y in enumerate(fnames):
        with open('feminine/%s'%y,'r') as f:
            for line in f:
                job,_,_,fr = line.split()
                fr = float(fr)
                if not job in D2:
                    D2[job] = [[yr.split('.')[0],0.] for yr in fnames]
                D2[job][j][1] = fr
    return D,D2
