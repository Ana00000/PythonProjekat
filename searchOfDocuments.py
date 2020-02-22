from typing import List, Any

import trie
import set


def find(root, logical_op, search):

    if logical_op == "OR" or logical_op == "or":

        if len(search) == 1:

            konacan_set, konacan_recnik = trie.find(root, search[0])
            return konacan_set, konacan_recnik

        elif len(search) == 2:

            set1, recnik1 = trie.find(root, search[0])
            set2, recnik2 = trie.find(root, search[1])

            konacan_set = set.Set()
            konacno = konacan_set.unija(set1).unija(set2)

            for kljuc2 in recnik2:

                if kljuc2 not in recnik1:

                    recnik1[kljuc2] = recnik2[kljuc2]

            return konacno, recnik1

        elif len(search) == 3:

            set1, recnik1 = trie.find(root, search[0])
            set2, recnik2 = trie.find(root, search[1])
            set3, recnik3 = trie.find(root, search[2])

            konacan_set = set.Set()
            konacno = konacan_set.unija(set1).unija(set2).unija(set3)

            for kljuc2 in recnik2:

                if kljuc2 not in recnik1:
                    recnik1[kljuc2] = recnik2[kljuc2]

                if kljuc2 not in recnik3:
                    recnik3[kljuc2] = recnik2[kljuc2]

            for kljuc1 in recnik1:

                if kljuc1 not in recnik3:
                    recnik3[kljuc1] = recnik1[kljuc1]

            return konacno, recnik1

    elif logical_op == "AND" or logical_op == "and":

        if len(search) == 2:

            set1, recnik1 = trie.find(root, search[0])
            set2, recnik2 = trie.find(root, search[1])

            konacan_set = set.Set()
            konacno = konacan_set.unija(set1).presek(set2)

            for kljuc1 in recnik1:

                if kljuc1 in recnik2:
                    recnik1[kljuc1] = recnik2[kljuc1]

            return konacno, recnik1

    elif logical_op == "NOT" or logical_op == "not":

        if len(search) == 2:

            set1, recnik1 = trie.find(root, search[0])
            set2, recnik2 = trie.find(root, search[1])

            konacan_set = set.Set()
            konacno = konacan_set.unija(set1).komplement(set2)

            za_brisanje: List[Any] = [kljuc for kljuc in recnik2 if kljuc in recnik1]

            for kljuc in za_brisanje:
                del recnik1[kljuc]

            return konacno, recnik1
