from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("A value is None")
        text_props = ""
        if self.tag == None:
            return self.value
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                for prop in self.props:
                    text_props += f' {prop}="{self.props[prop]}"'
                return f"<{self.tag}{text_props}>{self.value}</{self.tag}>"
