# Problem 10: Post and Profile classes

# Part (a): Post class
class Post:
    def __init__(self, caption):
        self.caption = caption
        self.likes = 0

    def get_likes(self):
        return self.likes

    def add_like(self):
        self.likes += 1

    def display(self):
        print(f"Caption: {self.caption}")

    def __str__(self):
        return f"Post(caption={self.caption}, likes={self.likes})"


# Part (b): Profile class
class Profile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def display_trending_posts(self):
        trending = [post for post in self.posts if post.get_likes() >= 10000]

        if not trending:
            print(f"{self.username} has no trending posts.")
        else:
            print(f"{self.username}'s trending posts:")
            for post in trending:
                print(f" - {post.caption} ({post.likes} likes)")

    def __str__(self):
        return f"Profile(username={self.username})"


# Part (c): Demonstration
if __name__ == "__main__":
    profile = Profile("maya_arts")
    post1 = Post("Sunset painting")
    post2 = Post("City lights")

    for _ in range(12000):
        post1.add_like()
    for _ in range(15000):
        post2.add_like()

    profile.add_post(post1)
    profile.add_post(post2)

    print(profile)
    print(post1)
    print(post2)
    profile.display_trending_posts()
