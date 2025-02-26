# Write a program that asks the user for his or her name, then enter a sentence that describes himself or herself. Once
# the user has entered the requested input, the program should create a HTML file, ex: "myHtml.html",  containing the
# input for a simple Web Page. Here is an example of the HTML content, using a sample input:
#
# <html>
# <head>
# </head>
# <body>
#    <center>
#        <h1>Julie Taylor</h1>
#    </center>
#    <hr />
#    I am a computer science major, a member of the jazz club,
#    and I hope to work as a mobile app developer after I graduate.
#    <hr />
# </body>
# </html>
#
# The task is to make a program that generates a custom html file, that can be viewed in a browser.
#
# Remember to use functions to structure your code.
import webbrowser


class WebpageGenerator:

    def __init__(self):
        self.state = "menu"

    def menu(self):
        print("""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬(¯`·._.··¸.-~*´¨¯¨`*·~-.,-(Webpage Generator 3000)-,.-~*´¨¯¨`*·~-.¸··._.·´¯)▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Create a HTML....................................1 ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Type in your name................................2 ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Describe yourself................................3 ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ View.............................................4 ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
        """)
        choice = int(input("pick your action and type it in"))
        if choice == 1:
            self.state = "create_html_file"
        elif choice == 2:
            self.state = "type_name"
        elif choice == 3:
            self.state = "describe"
        elif choice == 4:
            self.state = "webbrowser"
        else:
            print("Try again, we got work to do")
            self.state = "menu"

    def create_html_file(self, name, content):
        with open("myHtml.html", "w") as f:
            html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
    </head>
    <body>
    <button onclick="displayAlert()">Click me!</button>
    <center>
        <h1>{name}</h1>
    </center>
    <hr />
    {content}
    <hr />
    </body>
    </html>
    """
            f.write(html_content)
            self.state = "menu"

    def type_name(self):
        name = input("Enter your name for the HTML page: ")
        self.create_html_file(name, "")
        self.state = "menu"

    def describe(self):
        content = input("Enter your description for the HTML page: ")
        self.create_html_file("", content)
        self.state = "menu"

    def webbrowser(self):
        webbrowser.open_new_tab("myHtml.html")
        self.state = "menu"

    def run(self):
        while self.state != "exit":
            if self.state == "menu":
                self.menu()
            if self.state == "create_html_file":
                self.create_html_file("", "")
            if self.state == "type_name":
                self.type_name()
            if self.state == "describe":
                self.describe()
            if self.state == "webbrowser":
                self.webbrowser()


if __name__ == "__main__":
    manager = WebpageGenerator()
    manager.run()
