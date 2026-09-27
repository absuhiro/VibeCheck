from comment import Comment


class Hashtag:

    def __init__(self, name):
        self.name = name

    def display(self):
        return self.name


class Post:

    next_id = 1

    def __init__(self, content, user):

        self.post_id = Post.next_id
        Post.next_id += 1

        self.content = content
        self.user = user

        self.likes = 0
        self.comments = []

    def display(self):
        print(self.content)

    def like(self):
        self.likes += 1

    def add_comment(self, text):

        comment = Comment(text)

        self.comments.append(comment)

    def display_comments(self):

        print("Comments:")

        if len(self.comments) == 0:
            print("No comments yet.")

        else:
            for comment in self.comments:
                comment.display()