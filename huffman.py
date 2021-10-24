from __future__ import annotations

from typing import Optional


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

    def __lt__(self, other) -> bool:
        """Returns True if and only if self < other."""


def count_frequencies(filename: str) -> list[int]:
    """Reads the given file and counts the frequency of each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the frequency with which that character occured.
    """


def build_huffman_tree(frequencies: list[int]) -> Optional[HuffmanNode]:
    """Creates a Huffman tree of the characters with non-zero frequency.

    Returns the root of the tree.
    """


def create_codes(tree: Optional[HuffmanNode]) -> list[str]:
    """Traverses the tree creating the Huffman code for each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the Huffman code for that character.
    """


def create_header(frequencies: list[int]) -> str:
    """Returns the header for the compressed Huffman data.

    For example, given the file "aaaccbbbb", this would return:
    "97 3 98 4 99 2"
    """


def huffman_encode(in_filename: str, out_filename: str) -> None:
    """Encodes the data in the input file, writing the result to the
    output file."""
