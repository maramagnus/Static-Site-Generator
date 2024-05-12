import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

leaf_node_paragraph = LeafNode("p", "This is a paragraph")
leaf_node_link = LeafNode("a", "Click the damn Link", None, {"href": "https://www.sonicpiratesgr.com"})
leaf_node_no_val = LeafNode("p", None, None, None)
leaf_node_no_tag = LeafNode(None, "I have words, but no tag", None, None)

print(leaf_node_paragraph.to_html())
print(leaf_node_link.to_html())
print(leaf_node_no_tag.to_html())

