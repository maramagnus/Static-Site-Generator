class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list[object] = None, props: dict[str: str] = None):
        self.tag: str = tag
        self.value: str = value
        self.children: list[object] = children
        self.props: dict[str: str] = props
        
    def to_html(self):
        raise NotImplementedError("No Code")
    
    def props_to_html(self) -> str:
        ret_string = ""
        if self.props != None:
            for key in self.props:
                ret_string = ret_string + (f' {key}="{self.props[key]}"')
        return ret_string
            

    def __repr__(self) -> str:
        return f"HTMLNode:{self.tag, self.value, self.children, self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str: str] = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All Leaf Nodes Require a Value")
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"