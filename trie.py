from typing import Dict, Any

import set


class TrieNode(object):

    dict: Dict[Any, Any]

    def __init__(self, character: str):
        self.character = character
        self.children = []
        self.word_end = False
        self.dict = {}
        self.counter = 0
        self.set = set.Set()

    def is_leaf(self):
        return len(self.children) == 0


class Tree(object):

    def __init__(self):

        self.root = None

    def is_empty(self):

        return self.root is None

    def height(self, x):

        if x.is_leaf():

            return 0

        else:

            return 1 + max(self.height(c) for c in x.children)


def add(root, word: str, path):
    node = root

    for character in word:

        found_from_child = False

        for child in node.children:

            if child.character == character:
                node = child
                found_from_child = True
                break

        if not found_from_child:
            new_node = TrieNode(character)
            node.children.append(new_node)
            node = new_node

    node.word_end = True

    if path in node.dict:

        node.dict[path] += 1
        node.set.add(path)
        node.counter += 1

    else:

        node.dict[path] = 1
        node.set.add(path)
        node.counter += 1


def find(root, prefix: str):
    node = root
    set_page = set.Set

    if not root.children:
        return set_page, node.dict

    for character in prefix:

        character_found = False

        for child in node.children:

            if child.character == character:
                character_found = True
                node = child
                break

        if not character_found:
            return set_page, node.dict

    return node.set, node.dict
