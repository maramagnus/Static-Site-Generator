import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

HTML_node_1 = HTMLNode("h1", "This is a heading 1", None, {"href": "google.com"})
HTML_node_2 = HTMLNode("p", "This is a paragraph", None, {"href": "www.sonicpiratesgr.com"})
HTML_node_3 = HTMLNode("body", None, [HTML_node_1, HTML_node_2], None)
leaf_node = LeafNode("p", "This is a paragraph", None, {"href": "www.sonicpiratesgr.com"})
print(leaf_node.__repr__())
print(leaf_node.props_to_html())
