def like_or_dislike(events):
	state = "nothing"

	# Events are button names, not a number for range(); a repeated press toggles off.
	for event in events:
		if event == state:
			state = "nothing"
		else:
			state = event

	return state

# Test the function with a sample input
print(like_or_dislike(["dislike"])) # Expected output: "dislike"
print(like_or_dislike(["like", "like"])) # Expected output: "nothing"
print(like_or_dislike(["dislike", "like"])) # Expected output: "like"
print(like_or_dislike(["like", "dislike", "dislike"])) # Expected output: "nothing"
