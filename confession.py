from post import Post, Hashtag


class Confession(Post):

    def __init__(self, content, hashtags, user):

        super().__init__(content, user)

        self.hashtags = []

        for hashtag in hashtags:

            self.hashtags.append(
                Hashtag(hashtag)
            )

    def display(self):

        print("-------------------------")

        print("CONFESSION")

        print("Post ID:", self.post_id)

        print(
            "Anonymous:",
            self.user.display()
        )

        print(self.content)

        print("Hashtags:", end=" ")

        for hashtag in self.hashtags:

            print(
                hashtag.display(),
                end=" "
            )

        print()

        print("Likes:", self.likes)

        print("-------------------------")