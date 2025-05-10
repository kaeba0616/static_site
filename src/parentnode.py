from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children=[], props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        text_children = ""
        if self.tag == None:
            raise ValueError("A tag is None")

        if len(self.children) == 0:
            raise ValueError("Children are None")

        for child in self.children:
            text_children += child.to_html()
        return f"<{self.tag}>{text_children}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
