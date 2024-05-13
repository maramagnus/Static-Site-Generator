from htmlnode import ParentNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

node2 = ParentNode(
    "p",
    [LeafNode("a", "click the damn link", {"href": "https://www.sonicpiratesgr.com"})]
    )

node = ParentNode(
    "p",
    [
        node2,
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

print(node.to_html())
