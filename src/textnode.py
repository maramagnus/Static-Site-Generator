from typing import Self

class TextNode:
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        self.text: str = text
        self.text_type: str = text_type
        self.url: str = url

    def __eq__(self, other: Self) -> bool:
        return self.__dict__ == other.__dict__
        
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"