from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children=[], props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("A tag is None")

        elif len(self.children) == 0:
            raise ValueError("Children are None")

        else:
            text_children = ""
            for child in self.children:
                text_children += child.to_html()
            return f"<{self.tag}>{text_children}</{self.tag}>"
