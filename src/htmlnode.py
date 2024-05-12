class HTMLNode:
    def __main__(self, tag: str = None, value: str = None, children: list[object] = None, props: dict[str: str] = None):
        self.tag: str = tag
        self.value: str = value
        self.children: list[object] = children
        self.props: dict[str: str] = props
        
    def to_html(self):
        raise NotImplementedError("No Code")
    
    def props_to_html(self):
        pass

    def __repr__(self):
        pass