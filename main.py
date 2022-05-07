import jieba
from gensim import corpora, models, similarities

import core.io as io
import core.models as model

reg_map = io.getData()

chain = []
group = {}
index = 0

for k in reg_map.keys():
    chain.append(model.Container(key=reg_map[k], data=k))

while len(chain) != 0:
    group[index] = {}
    chain = model.chain_filter(chain)

    match_list = []
    for i in range(0, len(chain)):
        match_element = [word for word in jieba.cut(chain[i].key)]
        match_list.append(match_element)

    match_pattern = chain[0].key
    match_pattern = [word for word in jieba.cut(match_pattern) if word != ' ']

    dic = corpora.Dictionary(match_list)

    corpus = [dic.doc2bow(doc) for doc in match_list]

    match_pattern = dic.doc2bow(match_pattern)

    lsi = models.LsiModel(corpus)

    lib = similarities.SparseMatrixSimilarity(
        lsi[corpus], num_features=len(dic.keys()))

    sim = lib[lsi[match_pattern]]

    fmt_sim = sorted(enumerate(sim), key=lambda item: item[1])
    tmp = []

    for i in range(0, len(fmt_sim)):
        if fmt_sim[i][1] > 0.01:
            tmp.append(chain[fmt_sim[i][0]])

    for t in tmp:
        group[index][t.prototype] = t.data
        chain.remove(t)

    index += 1

io.writeData(group)
