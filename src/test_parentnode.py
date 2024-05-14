from htmlnode import ParentNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

lnode_title = LeafNode("title", "Page Title",)
lnode1 = LeafNode("b", "Bold text")
lnode2 = LeafNode(None, "Normal text")
lnode3 = LeafNode("i", "italic text")
lnode4 = LeafNode(None, "Normal text")
lnode5 = LeafNode("a", "click the damn link", {"href": "https://www.sonicpiratesgr.com"})
lnode_nested = LeafNode("blockquote", "Nested text, happy cats!")


pnode_head = ParentNode("head",[lnode_title],)
pnode_nested_deeper = ParentNode("**DEEP NEST**", [lnode_nested, lnode5, lnode_nested])
pnode_para_nest = ParentNode("p",[lnode_nested, lnode2, pnode_nested_deeper, lnode4, lnode_nested],)
pnode_para = ParentNode("p",[lnode1, pnode_para_nest, lnode2,lnode3, pnode_para_nest, lnode4,],)
pnode_body = ParentNode("body", [pnode_para],)
pnode_html = ParentNode("html",[pnode_head, pnode_body],)

print(pnode_html.to_html())
