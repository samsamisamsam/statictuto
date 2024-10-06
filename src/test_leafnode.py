import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_with_tag_and_value(self):
        node = LeafNode("This is a test", "p")
        self.assertEqual(node.to_html(), "<p>This is a test</p>")

    def test_leaf_node_with_props(self):
        node = LeafNode("Click me!", "a", {"href": "https://www.example.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">Click me!</a>')

    def test_leaf_node_without_tag(self):
        node = LeafNode("Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_node_with_empty_value(self):
        with self.assertRaises(ValueError):
            LeafNode("").to_html()

