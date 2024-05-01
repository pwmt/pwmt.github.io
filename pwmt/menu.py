import os

class MenuItem():
    "Represents a menu item"

    def __init__(self, caption, endpoint="#"):
        "Initializes the menu item"
        self.items = []
        self.endpoint = endpoint
        self.caption = caption

    def render(self):
        render_string = ""

        if len(self.items) != 0:
            render_string += (
                '<li class="dropdown">'
                '<a href="#" class="dropdown-toggle" data-toggle="dropdown">'
                + self.caption +
                '<i class="fa fa-angle-down"></i></a>'
                '<ul class="dropdown-menu">'
            )

            for item in self.items:
                render_string += item.render()

            render_string += '</ul>'
        else:
            render_string += '<li><a href="' + str(self.endpoint) + '">' + \
                str(self.caption) + '</a></li>'

        return render_string

    def addSubItem(self, item):
        "Adds an item to the menu"
        self.items.append(item)


class Menu():
    "Represents a menu"

    def __init__(self, html_class="nav"):
        "Initializes the menu"
        self.items = []
        self.html_class = html_class

    def addItem(self, item):
        "Adds an item to the menu"
        self.items.append(item)

    def render(self):
        render_string = '<ul class="' + self.html_class + '">'

        for item in self.items:
            render_string += item.render()

        render_string += '</ul>'

        return render_string
