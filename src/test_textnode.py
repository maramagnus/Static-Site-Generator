import unittest

from textnode import TextNode
from textnode import split_nodes_delimiter

"""class TextNodeTest(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("I like turtles", "bold")
        node2 = TextNode("I like turtles", "bold")
        self.assertEqual(node1, node2)"""

node1 = TextNode("I like **turtles**", "bold")
node2 = "I am not a TextNode"
print(split_nodes_delimiter([node1, node2], "**", "bold"))


"""if __name__ == "__main__":
    unittest.main()"""
