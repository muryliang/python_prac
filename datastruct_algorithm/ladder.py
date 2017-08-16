from graph import Graph

def buildGraph(wordFile):
    """ from a ladder file read in word and connect words if diff in only one char"""

    d = {}
    g = Graph()
    wfile = open(wordFile, "r")

    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in bucket:
            for word2 in bucket:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g
