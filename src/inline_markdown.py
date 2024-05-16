from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,

)

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