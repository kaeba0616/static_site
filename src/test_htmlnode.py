import unittest

from htmlnode import HTMLNode


class TESTHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello World",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode("div", "I enjoy hebi's song")
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(node.value, "I enjoy hebi's song")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "i am testing repr function",
            None,
            {
                "idol": "hebi",
            },
        )
        self.assertEqual(
            repr(node),
            "HTML(p, i am testing repr function, children: None, {'idol': 'hebi'})",
        )


if __name__ == "__main__":
    unittest.main()
