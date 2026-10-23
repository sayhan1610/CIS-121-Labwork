def design_rug(width, length, pattern='@'):
	# A default pattern lets the handout's two-argument example run successfully.
	# The loop must make one row per length; tabs did not create separate rows.
	rows = [pattern * width for _ in range(length)]
	return "Your rug is:\n" + "\n".join(rows)

print(design_rug(3, 5, '$')) # Expected output: "Your rug is:\n$$$\n$$$\n$$$\n$$$\n$$$"
print(design_rug(16, 5)) # Expected output: five rows of 16 @ characters

				 