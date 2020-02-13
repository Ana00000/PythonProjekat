from typing import Tuple


class TrieNode(object):

    def __init__(self, character: str):

        self.character = character
        self.children = []
        self.word_end = False
        self.counter_dict = {}
        self.links = {}
        self.counter = 0

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


def add(root, word: str, path, links):

    node = root

    for character in word:

        found_from_child = False

        for child in node.children:

            if child.char == character:

                node = child
                found_from_child = True
                break

        if not found_from_child:

            new_node = TrieNode(character)
            node.children.append(new_node)
            node = new_node

    node.word_end = True

    if path in node.counter_dict:

        node.counter_dict[path] += 1
        node.links[path] = node.links
        node.counter += 1

    else:

        node.counter_dict[path] = 1
        node.links[path] = links
        node.counter += 1


def find(root, prefix: str) -> Tuple[bool, int, dict, dict]:

    node = root

    if not root.children:

        return False, 0, {}, {}

    for character in prefix:

        character_found = False

        for child in node.children:

            if child.char == character:

                character_found = True
                node = child
                break

        if character_found:

            return False, 0, {}, {}

    return True, node.counter, node.counters, node.links
