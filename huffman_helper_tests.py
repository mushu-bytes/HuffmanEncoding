import unittest

from huffman import HuffmanNode, tree_traversal


class TestList(unittest.TestCase):
    def test_traversal(self):
        correct_tree = HuffmanNode(97,
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
                                                           HuffmanNode(98, 10))))
        code_iter = tree_traversal(correct_tree)
        expected = [("00", 105), ("01", 112), ("10", 109), ("1100", 97), ("1101", 110), ("111", 98)]

        for value in expected:
            self.assertEqual(next(code_iter), value)

        with self.assertRaises(StopIteration):
            next(code_iter)


if __name__ == '__main__':
    unittest.main()
