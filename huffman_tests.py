import unittest
import subprocess

# NOTE: Do not import anything else from huffman.  If you do, your tests
# will crash when I test them.  You shouldn't need to test your helper
# functions directly, just via testing the required functions.
from huffman import (
    HuffmanNode, count_frequencies, build_huffman_tree, create_codes,
    create_header, huffman_encode)


class TestList(unittest.TestCase):
    def test_count_frequencies_01(self):
        frequencies = count_frequencies("text_files/file2.txt")
        expected = [0, 2, 4, 8, 16, 0, 2, 0]

        self.assertEqual(frequencies[96:104], expected)

    def test_count_frequencies_multiline(self):
        # should we be counting newline chars. it counts multi lines
        frequencies = count_frequencies("text_files/multiline.txt")

    def test_node_lt_01(self):
        node1 = HuffmanNode(97, 10)
        node2 = HuffmanNode(65, 20)

        self.assertLess(node1, node2)
        self.assertGreater(node2, node1)

    def test_node_equality(self):
        node1 = HuffmanNode(97, 10)
        node2 = HuffmanNode(97, 10)

        self.assertEqual(node1, node2)

    def test_build_huffman_tree_01(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10

        huffman_tree = build_huffman_tree(frequencies)

        # NOTE: This also requires a working __eq__ for your HuffmanNode
        self.assertEqual(
            huffman_tree,
            HuffmanNode(97, 15, HuffmanNode(97, 5), HuffmanNode(98, 10))
        )

    def test_build_huffman_tree_02(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10
        frequencies[112] = 15
        frequencies[109] = 16
        frequencies[110] = 5
        frequencies[105] = 10

        huffman_tree = build_huffman_tree(frequencies)

        # NOTE: This also requires a working __eq__ for your HuffmanNode

        self.assertEqual(
            huffman_tree,
            HuffmanNode(97,
                        61,
                        HuffmanNode(105,
                                    25,
                                    HuffmanNode(105, 10),
                                    HuffmanNode(112, 15)),
                        HuffmanNode(97,
                                    36,
                                    HuffmanNode(109, 16),
                                    HuffmanNode(97,
                                                20,
                                                HuffmanNode(97,
                                                            10,
                                                            HuffmanNode(97, 5),
                                                            HuffmanNode(110, 5)),
                                                HuffmanNode(98, 10)))))

    def test_empty_frequencies(self):
        frequencies = [0] * 256
        huffman_tree = build_huffman_tree(frequencies)

        self.assertEqual(huffman_tree, None)

    def test_one_node(self):
        frequencies = [0] * 256
        frequencies[113] = 23

        huffman_tree = build_huffman_tree(frequencies)

        self.assertEqual(huffman_tree, HuffmanNode(113, 23))

    def test_create_codes_01(self):
        huffman_tree = HuffmanNode(
            97, 15,
            HuffmanNode(97, 5),
            HuffmanNode(98, 10)
        )

        codes = create_codes(huffman_tree)
        self.assertEqual(codes[ord('a')], '0')
        self.assertEqual(codes[ord('b')], '1')

    """
    def test_create_header_01(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10

        self.assertEqual(create_header(frequencies), "97 5 98 10")

    def test_huffman_encode_01(self):
        huffman_encode("text_files/file1.txt", "text_files/file1_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/file1_out.txt',
             'text_files/file1_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)"""


if __name__ == '__main__':
    unittest.main()
