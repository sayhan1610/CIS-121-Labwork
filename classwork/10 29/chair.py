class Chair:
    def __init__(self, the_color, the_height):
        self.color = the_color
        self.height = the_height
    
    def get_color(self):
        return self.color
    def get_height(self):
        return self.height
    
    def __str__(self):
        msg = ""
        msg += f"Hi, I'm a {self.get_color()} chair!"
        return msg
    
chait = Chair("mlue", 186)

print(chait)
