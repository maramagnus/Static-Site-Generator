import unittest

from textnode import TextNode
from textnode import split_nodes_delimiter

"""class TextNodeTest(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("I like turtles", "bold")
        node2 = TextNode("I like turtles", "bold")
        self.assertEqual(node1, node2)"""

node1 = TextNode("I like **turtles** contains a bolded word", "text")
node2 = TextNode("There are many cats, but **Mara** was special", "text")
node3 = TextNode("*All of this text is italic*", "text")
node4 = TextNode("the world is far *poorer* for the loss", "text")
node5 = TextNode("This line contains `code snippets`", "text")
node6 = TextNode("The solution to my problem turned out to be `this code block here`", "text")

bold_nodes = [node1, node2]
italic_nodes = [node3, node4]
code_nodes = [node5, node6]

print(split_nodes_delimiter(bold_nodes, "**", "bold"))
print(split_nodes_delimiter(italic_nodes, "*", "italic"))
print(split_nodes_delimiter(code_nodes, "`", "code"))


"""if __name__ == "__main__":
    unittest.main()"""
