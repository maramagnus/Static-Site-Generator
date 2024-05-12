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
        for key in self.props:
            ret_string = ret_string + (f" {key} {self.props[key]}")
        return ret_string
            

    def __repr__(self) -> str:
        return f"HTMLNode:{self.tag, self.value, self.children, self.props}"