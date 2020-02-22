import os
import trie
from analyzer import Parser


def parsing(root_dir):
    root = trie.TrieNode("*")
    found = 0

    for subdir, dirs, files in os.walk(root_dir, topdown=True):

        for file in files:

            if file.endswith('.html'):

                found = 1
                par = Parser()
                relative_path = os.path.join(subdir, file)
                file_path = os.path.abspath(relative_path)
                par.parse(file_path)

                for word in par.words:
                    trie.add(root, word.lower(), os.path.join(subdir, file))

    if found == 0:
        print("Ne postoji html dokument u korenskom direktorijumu: ", root_dir)
        return False, root

    return True, root
