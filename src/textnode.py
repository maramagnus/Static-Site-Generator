from typing import Self

class TextNode:
    def __init__(self, text: str, text_type: str, url = None):
        self.text: str = text
        self.text_type: str = text_type
        self.url = url

    def __eq__(self, other: Self):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"