from typing import List, Any

import trie
import set


def find(root, logical_op, search):

    konacan_set = set.Set()

    if logical_op == "OR":

        if len(search) == 1:

            konacan_set, konacan_recnik = trie.find(root, search[0])
            return konacan_set, konacan_recnik

        else:

            set1, recnik1 = trie.find(root, search[0])
            del search[0]

            for word in search:

                set2, recnik2 = trie.find(root, word)
                konacan_set = set1 | set2

                for kljuc2 in recnik2:

                    if kljuc2 not in recnik1:

                        recnik1[kljuc2] = recnik2[kljuc2]

            return konacan_set, recnik1

    elif logical_op == "AND":

        if len(search) == 2:

            set1, recnik1 = trie.find(root, search[0])
            set2, recnik2 = trie.find(root, search[1])
            konacan_set = set1 & set2

            for kljuc1 in recnik1:

                if kljuc1 in recnik2:

                    recnik1[kljuc1] = recnik2[kljuc1]

            return konacan_set, recnik1

    elif logical_op == "NOT":

        if len(search) == 2:

            set1, recnik1 = trie.find(root, search[0])
            set2, recnik2 = trie.find(root, search[1])

            konacan_set = set1.komplement(set2)
            za_brisanje: List[Any] = [kljuc for kljuc in recnik2 if kljuc in recnik1]

            for kljuc in za_brisanje:
                del recnik1[kljuc]

            return konacan_set, recnik1
