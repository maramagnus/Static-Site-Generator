from typing import Self
from htmlnode import LeafNode

class TextNode:
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        self.text: str = text
        self.text_type: str = text_type
        self.url: str = url

    def __eq__(self, other: Self) -> bool:
        return self.__dict__ == other.__dict__
        
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text,)
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text,)
    if text_node.text_type == "italic":
        return LeafNode("i", text_node.text,)
    if text_node.text_type == "code":
        return LeafNode("code", text_node.text,)
    if text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("Invalid Text Type")

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str) -> list[TextNode]:
    ret_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != "text":
            ret_nodes.append(node)
        else:    
            split_node: list[str] = (node.text).split(delimiter)
            if len(split_node) % 2 == 0:
                raise Exception("Invalid Markdown syntax: Missing a closing delimiter.")
            
            for i in range(0, len(split_node)):
                if split_node[i] == "":
                    continue
                if i % 2 == 0:
                    new_node = TextNode(split_node[i], "text")
                if i % 2 != 0:
                    new_node = TextNode(split_node[i], text_type)
                ret_nodes.append(new_node)
    return ret_nodes
