import unittest
from htmlnode import HTMLNode

HTML_node_1 = HTMLNode("h1", "This is a heading 1", None, {"href": "google.com"})
HTML_node_2 = HTMLNode("p", "This is a paragraph", None, {"href": "www.sonicpiratesgr.com"})
HTML_node_3 = HTMLNode("body", None, [HTML_node_1, HTML_node_2], None)

print(HTML_node_1.__repr__())
print(HTML_node_2.props_to_html())
print(HTML_node_3.__repr__())
print(HTML_node_1.props_to_html())