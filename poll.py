from post import Post


class Poll(Post):

    def __init__(self, question, options, user):

        super().__init__(question, user)

        self.options = options

        self.votes = {}

        for option in options:

            self.votes[option] = 0

    def vote(self, option):

        if option in self.votes:

            self.votes[option] += 1

        else:

            print("Invalid option!")

    def get_percentage(self, option):

        total_votes = sum(
            self.votes.values()
        )

        if total_votes == 0:

            return 0

        return (
            self.votes[option]
            / total_votes
        ) * 100

    def get_bar(self, percentage):

        bar_length = int(
            percentage / 5
        )

        return "█" * bar_length

    def display(self):

        print("-------------------------")

        print("POLL")

        print("Post ID:", self.post_id)

        print(
            "Anonymous:",
            self.user.display()
        )

        print(self.content)

        total_votes = sum(
            self.votes.values()
        )

        print(
            "Total votes:",
            total_votes
        )

        for option in self.options:

            percentage = self.get_percentage(
                option
            )

            bar = self.get_bar(
                percentage
            )

            print(
                option,
                bar,
                f"{percentage:.1f}%"
            )

        print("Likes:", self.likes)

        print("-------------------------")