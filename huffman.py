from __future__ import annotations

from collections import Iterator
from typing import Optional, Any

from ordered_list import (
    OrderedList, insert, pop, size)


class HuffmanNode:
    """Represents a node in a Huffman tree.

    Attributes:
        char: The character as an integer ASCII value
        frequency: The frequency of the character in the file
        left: The left Huffman sub-tree
        right: The right Huffman sub-tree
    """

    def __init__(
            self,
            char: int,
            frequency: int,
            left: Optional[HuffmanNode] = None,
            right: Optional[HuffmanNode] = None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        """Returns True if and only if self and other are equal."""
        return (
                isinstance(other, HuffmanNode) and
                self.frequency == other.frequency and
                self.char == other.char and
                self.left == other.left and
                self.right == other.right
        )

    def __lt__(self, other) -> bool:
        """Returns True if and only if self < other."""

        if self.frequency == other.frequency:
            return self.char < other.char

        return self.frequency < other.frequency


def count_frequencies(filename: str) -> list[int]:
    """Reads the given file and counts the frequency of each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the frequency with which that character occured.
    """
    frequency = [0] * 256

    with open(filename) as file:
        for line_of_text in file:
            for char in line_of_text:
                frequency[ord(char)] += 1
    return frequency


def build_huffman_tree(frequencies: list[int]) -> Optional[HuffmanNode]:
    """Creates a Huffman tree of the characters with non-zero frequency.

    Returns the root of the tree.
    """
    # init an ordered list and add all the non zero chars into it
    ordered_list = OrderedList()
    # the index is the char in ascii format
    for ascii_val in range(len(frequencies)):
        if frequencies[ascii_val] != 0:
            insert(ordered_list,
                   HuffmanNode(ascii_val, frequencies[ascii_val]))

    # create a new node with the least two nodes as children
    # lesser of the two will be on the left
    # will take the smallest of the two ascii vals.

    if size(ordered_list) == 0:
        return None

    while size(ordered_list) > 1:
        lesser_node = pop(ordered_list, 0)
        greater_node = pop(ordered_list, 0)
        new_frequency = lesser_node.frequency + greater_node.frequency
        new_char = 0
        if lesser_node.char > greater_node.char:
            new_char = greater_node.char
        else:
            new_char = lesser_node.char
        insert(ordered_list,
               HuffmanNode(new_char, new_frequency, lesser_node, greater_node))
    # remember to check whether the list is empty or at one
    if size(ordered_list) == 1:
        return pop(ordered_list, 0)


def tree_traversal(tree: Optional[HuffmanNode], str="") -> Iterator[Any]:
    if tree.left is None and tree.right is None:
        yield str, tree.char
        return None
    yield from tree_traversal(tree.left, str + "0")
    yield from tree_traversal(tree.right, str + "1")


def create_codes(tree: Optional[HuffmanNode]) -> list[str]:
    """Traverses the tree creating the Huffman code for each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the Huffman code for that character.

    Think about if the tree is None, tree has only 1 Node, and so on
    """
    codes = [""] * 256
    if tree is None:
        return codes

    for tup in tree_traversal(tree):
        codes[tup[1]] = tup[0]

    return codes


def create_header(frequencies: list[int]) -> str:
    """Returns the header for the compressed Huffman data.

    For example, given the file "aaaccbbbb", this would return:
    "97 3 98 4 99 2"

    What happens if the frequencies are all 0, maybe don't call it at all?
    """
    header = ""

    for ascii in range(len(frequencies)):
        if frequencies[ascii] != 0:
            header = header + str(ascii) + " " + str(frequencies[ascii]) + " "

    return header[:-1]


def huffman_encode(in_filename: str, out_filename: str) -> None:
    """Encodes the data in the input file, writing the result to the
    output file."""
    frequencies = count_frequencies(in_filename)
    tree = build_huffman_tree(frequencies)
    header = create_header(frequencies)
    # if empty file
    if tree is None:
        with open(out_filename, "w") as file:
            file.write(header)
            file.write("\n")
        return None
        # if single char

    codes = create_codes(tree)

    if tree.left is None and tree.right is None:
        with open(out_filename, "w") as file:
            file.write(header)
            file.write("\n")

        return None

    with open(out_filename, 'w') as file:
        file.write(header)
        file.write("\n")
        with open(in_filename, 'r') as file_two:
            for line_of_text in file_two:
                for char in line_of_text:
                    file.write(codes[ord(char)])

    return None
