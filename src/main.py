from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text,)
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text,)
    if text_node.text_type == "italic":
        pass
    if text_node.text_type == "code":
        pass
    if text_node.text_type == "link":
        pass
    if text_node.text_type == "image":
        pass

    
def main():
    node_tester1 = TextNode("I like turtles", "italic", "https://boot.dev")
    node_tester2 = TextNode("I like turtles", "bold", "https://google.com")
    node_tester3 = TextNode("I like turtles", "italic", "https://boot.dev")
    html_node_test1 = HTMLNode("h1", "I Like Turtles", None, {"href": "https://www.sonicpiratesgr.com"})
    
    print(node_tester1.__eq__(node_tester3))
    print(html_node_test1.__repr__())
    print(html_node_test1.props_to_html())

if __name__ == "__main__":
    main()
