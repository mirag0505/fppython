from pymonad.reader import Compose
from pymonad.tools import curry

# 3.1.

@curry(2)
def tag(htmlTag: str,  text: str) -> str:
    return f"<{htmlTag}>{text}<{htmlTag}>"

def bold(text: str):
    return(tag('b', text))
    
def italic(text: str):
    return(tag('i', text))

bold("1231")
italic("1231")

# 3.2.
@curry(3)
def newTag(htmlTag: str, attr: dict, text: str) -> str:
    attr_list = []
    for key, value in attr.items():
        attr_str = f'{key}="{value}"'
        attr_list.append(attr_str)
    
    attributes = ' '.join(attr_list)
    
    return f"<{htmlTag} {attributes}>{text}</{htmlTag}>"

newTag('li', {'class': 'list-group'}, 'item 23')

