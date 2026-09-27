class Feed:

    def __init__(self):

        self.posts = []

    def add_post(self, post):

        self.posts.append(post)

    def display(self):

        print("\n========== FEED ==========")

        if len(self.posts) == 0:

            print("No posts yet.")

        else:

            for post in self.posts:

                post.display()

                post.display_comments()

        print("===========================")