import os
import trie
from Graph import Graph
from analyzer import Parser
graph = None


def parsing(root_dir):
    global graph
    graph = Graph()
    root = trie.TrieNode("*")
    found = 0

    for subdir, dirs, files in os.walk(root_dir, topdown=True):

        for file in files:

            if file.endswith('.html'):
                print(file)
                found = 1
                par = Parser()
                relative_path = os.path.join(subdir, file)
                file_path = os.path.abspath(relative_path)
                par.parse(file_path)

                # ubacivanje html stranica u graf (ubacivanje svih verteksa)
                graph.insert_vertex(file_path, par.links)

                for word in par.words:
                    trie.add(root, word.lower(), os.path.join(subdir, file))

    if found == 0:
        print("Ne postoji html dokument u korenskom direktorijumu: ", root_dir)
        return False, root

    # ubacivanje edgova u graph
    verteksi = graph.vertices()

    for verteks in verteksi:   # prolazimo kroz sve vertekse
        links = verteks.get_links()   # svi njegovi linkovi
        for link in links:
            for verteks2 in verteksi:
                if verteks2.get_path() == link:
                    graph.insert_edge(verteks, verteks2)
                    break


    return True, root, graph
