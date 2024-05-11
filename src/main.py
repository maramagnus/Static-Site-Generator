from textnode import TextNode

def main():
    node_tester1 = TextNode("I like turtles", "italic", "https://boot.dev")
    node_tester2 = TextNode("I like turtles", "bold", "https://google.com")
    node_tester3 = TextNode("I like turtles", "italic", "https://boot.dev")
    
    print(node_tester2.__repr__())
    print(node_tester1.__eq__(node_tester3))

main()
