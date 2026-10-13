# Problem 12: Determine the final state of a like/dislike button sequence.

def like_or_dislike(events):
    """Return the final state after processing the events list."""
    state = "nothing"
    for event in events:
        if event == state:
            state = "nothing"
        else:
            state = event
    return state


if __name__ == "__main__":
    print(like_or_dislike(["dislike"]))
    print(like_or_dislike(["like", "like"]))
    print(like_or_dislike(["dislike", "like"]))
    print(like_or_dislike(["like", "dislike", "dislike"]))
