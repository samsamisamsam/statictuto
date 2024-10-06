class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == {}:
            return ""
        html_tags = ""
        for key, value in self.props.items():
            html_tags += f'{key}="{value}" '
        html_tags = html_tags.rstrip(' ')
        return ' ' + html_tags
    
    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"