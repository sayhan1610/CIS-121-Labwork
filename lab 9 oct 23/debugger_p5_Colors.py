class ColorRGB:
	def __init__(self, red, green, blue):
		# Instance methods need self so construction can store the three channels.
		self.red = red
		self.green = green
		self.blue = blue
	
	def get_red(self):
		return self.red
	
	def set_red(self, red):
		self.red = red
	
	def get_green(self):
		return self.green
	
	def set_green(self, green):
		# Assigning to the parameter left the stored color unchanged.
		self.green = green
	
	def get_blue(self):
		return self.blue
	
	def set_blue(self, blue):
		self.blue = blue
	
	def to_grayscale(self):
		# The exercise's expected grayscale is the arithmetic mean of RGB channels.
		return (self.red + self.green + self.blue) / 3
	
# Test the function with a sample input
color = ColorRGB(100, 150, 200)
print(color.get_red()) # Expected output: 100
print(color.get_green()) # Expected output: 150
print(color.get_blue()) # Expected output: 200
print(color.to_grayscale()) # Expected output: 150.0
print(color.set_green(90)) # Expected output: None (setter method does not return anything)
print(color.get_green()) # Expected output: 90 (after setting green to 90)