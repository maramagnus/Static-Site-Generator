import unittest

from textnode import TextNode

class TextNodeTest(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("I like turtles", "bold")
        node2 = TextNode("I like turtles", "bold")
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
