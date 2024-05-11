class TextNode:
    def __init__(self, text: str, text_type: str, url = None):
        self.text: str = text
        self.text_type: str = text_type
        self.url = url

    def __eq__(self, other_node):
        if (
            self.text == other_node.text 
            and self.text_type == other_node.text_type
            and self.url == other_node.url
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"