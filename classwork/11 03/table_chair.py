# make a blueprint for a table,
# build an actual table,
# make some chairs for the table,
# the chairs could be any number, added or removed as needed


class Chair:
    def __init__(self, color, height):
        self.color = color
        self.height = height

    # getters
    def get_color(self):
        return self.color

    def get_height(self):
        return self.height

    # setters
    def set_color(self, new_color):
        self.color = new_color

    def set_height(self, new_height):
        self.height = new_height


class Table:
    def __init__(self, color="black", length=0, width=0):
        self.color = color
        self.length = length
        self.width = width
        self.chairs = []

    # getters
    def get_color(self):
        return self.color

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    # setters
    def set_color(self, new_color):
        self.color = new_color

    def set_length(self, new_length):
        self.length = new_length

    def set_width(self, new_width):
        self.width = new_width

    def add_chair(self, new_chair):
        if not isinstance(new_chair, Chair):
            raise TypeError("new_chair must be a Chair object")
        self.chairs.append(new_chair)

    def remove_chair(self, chair_to_remove):
        if chair_to_remove in self.chairs:
            self.chairs.remove(chair_to_remove)
            return True
        return False

    def show_chairs(self):
        print(f"Chairs for the {self.get_color()} table:")
        if not self.chairs:
            print(" - No chairs yet")
            return self.chairs

        for chair in self.chairs:
            print(f" - {chair.get_color()} chair ({chair.get_height()} in)")
        return self.chairs

    def __add__(self, other):
        if not isinstance(other, Table):
            return NotImplemented

        combined_table = Table(self.get_color(), self.get_length(), self.get_width())
        combined_table.chairs = self.chairs + other.chairs
        return combined_table


class DiningSet:
    def __init__(self, a_table):
        self.table = a_table

    @property
    def chair_list(self):
        return self.table.chairs

    def add_chair(self, new_chair):
        self.table.add_chair(new_chair)

    def show_chairs(self):
        self.table.show_chairs()


# Print Statements to test the classes
print("Creating a table and chairs...")
my_table = Table("brown", 60, 30)
print(f"Table color: {my_table.get_color()}, length: {my_table.get_length()}, width: {my_table.get_width()}")
chair1 = Chair("red", 18)
new_chair = Chair("blue", 20)
dining_set = DiningSet(my_table)
dining_set.add_chair(chair1)
dining_set.add_chair(new_chair)
dining_set.show_chairs()

print("\nCombining tables...")
table1 = Table()
table1.add_chair(Chair("blue", 15))
table1.add_chair(Chair("green", 15))

table2 = Table()
table2.add_chair(Chair("red", 15))
table2.add_chair(Chair("yellow", 15))

table3 = table1 + table2

table3.show_chairs()  # Should show blue, green, red, yellow chairs