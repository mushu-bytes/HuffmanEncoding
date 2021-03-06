import unittest
import subprocess

# NOTE: Do not import anything else from huffman.  If you do, your tests
# will crash when I test them.  You shouldn't need to test your helper
# functions directly, just via testing the required functions.
from huffman import (
    HuffmanNode, count_frequencies, build_huffman_tree, create_codes,
    create_header, huffman_encode, parse_header, huffman_decode)


class TestList(unittest.TestCase):
    def test_count_frequencies_01(self):
        frequencies = count_frequencies("text_files/file2.txt")
        expected = [0, 2, 4, 8, 16, 0, 2, 0]

        self.assertEqual(frequencies[96:104], expected)

    def test_node_lt_01(self):
        node1 = HuffmanNode(97, 10)
        node2 = HuffmanNode(65, 20)

        self.assertLess(node1, node2)
        self.assertGreater(node2, node1)

    def test_node_lt_02(self):
        node1 = HuffmanNode(220, 5)
        node2 = HuffmanNode(195, 5)

        self.assertLess(node2, node1)
        self.assertGreater(node1, node2)

    def test_node_lt_03(self):
        node1 = HuffmanNode(220, 5)
        node2 = HuffmanNode(225, 15)

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

    def test_node_equality_02(self):
        node1 = HuffmanNode(97, 10, HuffmanNode(98, 7))
        node2 = HuffmanNode(97, 10)

        self.assertNotEqual(node1, node2)

    def test_node_equality_03(self):
        node1 = HuffmanNode(97, 10, None, HuffmanNode(98, 3))
        node2 = HuffmanNode(97, 10)

        self.assertNotEqual(node1, node2)

    def test_node_equality_04(self):
        node1 = HuffmanNode(97, 10, None, HuffmanNode(98, 3))
        node2 = HuffmanNode(97, 10, None, HuffmanNode(98, 3))

        self.assertEqual(node1, node2)

    def test_node_equality_05(self):
        node1 = HuffmanNode(97,
                            10,
                            HuffmanNode(97,
                                        2,
                                        HuffmanNode(100, 12),
                                        HuffmanNode(10, 4)),
                            HuffmanNode(98, 3))
        node2 = HuffmanNode(97, 10, None, HuffmanNode(98, 3))

        self.assertNotEqual(node1, node2)

    def test_node_equality_06(self):
        node1 = HuffmanNode(97,
                            10,
                            HuffmanNode(97,
                                        2,
                                        HuffmanNode(100, 12),
                                        HuffmanNode(10, 4)),
                            HuffmanNode(98, 3))
        node2 = HuffmanNode(97,
                            10,
                            HuffmanNode(97,
                                        2,
                                        HuffmanNode(100, 12),
                                        HuffmanNode(10, 4)),
                            HuffmanNode(98, 3))

        self.assertEqual(node1, node2)

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

    def test_create_codes_02(self):
        huffman_tree = None
        codes = create_codes(huffman_tree)

        self.assertEqual(codes, [''] * 256)

    def test_create_codes_03(self):
        huffman_tree = HuffmanNode(97, 1, None, None)
        codes = create_codes(huffman_tree)

        print(codes)

    def test_create_header_01(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10

        self.assertEqual(create_header(frequencies), "97 5 98 10")

    def test_declaration(self):
        huffman_encode("text_files/declaration.txt", "text_files/dec_out.txt")

        result = subprocess.run(
            ["diff",
             "--strip-trailing-cr",
             "text_files/dec_out.txt",
             "text_files/declaration_soln.txt"],
            check=False,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

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
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_huffman_file_two(self):
        huffman_encode("text_files/file2.txt", "text_files/file_two_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/file_two_out.txt',
             'text_files/file2_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_huffman_empty(self):
        huffman_encode("text_files/empty.txt", "text_files/empty_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/empty_out.txt',
             'text_files/empty_file_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_huffman_one_node(self):
        huffman_encode("text_files/one.txt", "text_files/one_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/one_out.txt',
             'text_files/one_node_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_huffman_single_char(self):
        huffman_encode("text_files/single.txt", "text_files/single_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/single_out.txt',
             'text_files/single_char_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    def test_multi_line(self):
        huffman_encode("text_files/multiline.txt", "text_files/m_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/m_out.txt',
             'text_files/multiline_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    def test_new_line(self):
        huffman_encode("text_files/new_line.txt", "text_files/new_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/new_out.txt',
             'text_files/new_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    def test_parse_header_01(self):
        header = "97 2 98 4 99 8 100 16 102 2\n"

        frequencies = parse_header(header)
        expected = [0, 2, 4, 8, 16, 0, 2, 0]

        self.assertEqual(frequencies[96:104], expected)

    def test_parse_header_02(self):
        header = "97 2 98 4 99 8 100 16 102 2 103 91\n"

        frequencies = parse_header(header)
        expected = [0, 2, 4, 8, 16, 0, 2, 91]

        self.assertEqual(frequencies[96:104], expected)

    def test_parse_header_03(self):
        header = "97 2 98 4 99 8 100 16 102 2 103 91 104 6\n"

        frequencies = parse_header(header)
        expected = [0, 2, 4, 8, 16, 0, 2, 91, 6]

        self.assertEqual(frequencies[96:105], expected)

    def test_parse_header_04(self):
        header = "97 2 98 4 99 8 100 16\n"

        frequencies = parse_header(header)
        expected = [0, 2, 4, 8, 16]

        self.assertEqual(frequencies[96:101], expected)

    def test_parse_header_05(self):
        header = "97 2\n"

        frequencies = parse_header(header)
        expected = 2

        self.assertEqual(frequencies[97], expected)

    def test_parse_header_empty(self):
        header = ""

        frequencies = parse_header(header)
        expected = [0] * 256

        self.assertEqual(frequencies, expected)

    def test_huffman_decode_01(self):
        huffman_decode(
            "text_files/file1_soln.txt", "text_files/file1_decoded.txt")

        with open("text_files/file1_decoded.txt") as student_out, \
                open("text_files/file1.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_dec(self):
        huffman_decode(
            "text_files/declaration_soln.txt", "text_files/dec_decoded.txt")

        with open("text_files/dec_decoded.txt") as student_out, \
                open("text_files/declaration.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_empty(self):
        huffman_decode(
            "text_files/empty_file_soln.txt", "text_files/empty_decoded.txt")

        with open("text_files/empty_decoded.txt") as student_out, \
                open("text_files/empty.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_single_char(self):
        huffman_decode(
            "text_files/single_char_soln.txt", "text_files/single_decoded.txt")

        with open("text_files/single_decoded.txt") as student_out, \
                open("text_files/single.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_one_char(self):
        huffman_decode(
            "text_files/one_node_soln.txt", "text_files/one_decoded.txt")

        with open("text_files/one_decoded.txt") as student_out, \
                open("text_files/one.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())


if __name__ == '__main__':
    unittest.main()
