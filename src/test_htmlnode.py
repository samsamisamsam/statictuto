import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_props(self):
        node = HTMLNode(props={"rel": "stylesheet", "href": "styles.css"})
        result = node.props_to_html()
        expected = ' rel="stylesheet" href="styles.css"'
        self.assertEqual(result, expected)

    def test_props_to_html_empty(self):
        node = HTMLNode()
        result = node.props_to_html()
        expected = ""
        self.assertEqual(result, expected)

    def test_node_element(self):
        node = HTMLNode("p", "This is a paragraph", ["tr", "td"],
                        {"rel": "stylesheet", "href": "styles.css"})
        result = repr(node)
        expected = "tag = p, value = This is a paragraph, children = ['tr', 'td'], props = {'rel': 'stylesheet', 'href': 'styles.css'}"
        self.assertEqual(result, expected)