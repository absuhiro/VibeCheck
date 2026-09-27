import json
from username import User
from post import Post
from confession import Confession
from poll import Poll
from feed import Feed

def save_data(feed):

    data = []

    for post in feed.posts:

        post_data = {
            "id": post.post_id,
            "type": type(post).__name__,
            "content": post.content,
            "alias": post.user.alias,
            "likes": post.likes,
            "comments": []
        }

        # Save comments
        for comment in post.comments:
            post_data["comments"].append(comment.text)

        # Save confession data
        if isinstance(post, Confession):

            post_data["hashtags"] = []

            for hashtag in post.hashtags:
                post_data["hashtags"].append(hashtag.name)

        # Save poll data
        elif isinstance(post, Poll):

            post_data["options"] = post.options
            post_data["votes"] = post.votes

        data.append(post_data)

    with open("vibes.json", "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

def load_data(feed):

    try:

        with open("vibes.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:

        return

    highest_id = 0

    for post_data in data:

        user = User()

        # Restore the old anonymous alias
        user.alias = post_data["alias"]

        if post_data["type"] == "Confession":

            post = Confession(
                post_data["content"],
                post_data["hashtags"],
                user
            )

        elif post_data["type"] == "Poll":

            post = Poll(
                post_data["content"],
                post_data["options"],
                user
            )

            post.votes = post_data["votes"]

        else:

            continue

        post.post_id = post_data["id"]

        post.likes = post_data["likes"]

        # Restore comments
        for comment in post_data["comments"]:

            post.add_comment(comment)

        feed.add_post(post)

        if post.post_id > highest_id:

            highest_id = post.post_id

    Post.next_id = highest_id + 1

def show_menu():

    print("\n========== VIBECHECK ==========")

    print("1. Create Confession")
    print("2. Create Poll")
    print("3. View Feed")
    print("4. Vote on Poll")
    print("5. Like a Post")
    print("6. Add Comment")
    print("7. Exit")

    print("===============================")


def create_confession(user, feed):

    content = input(
        "Enter your confession: "
    )

    hashtag_input = input(
        "Enter hashtags separated by spaces: "
    )

    hashtags = hashtag_input.split()

    confession = Confession(
        content,
        hashtags,
        user
    )

    feed.add_post(confession)

    print("\nConfession created!")

    confession.display()


def create_poll(user, feed):

    question = input(
        "Enter your poll question: "
    )

    print("\nEnter poll options one by one.")
    print("Type 'done' when you have finished.")

    options = []

    while True:

        option = input("Enter option: ")

        if option.lower() == "done":
            break

        if option.strip() != "":
            options.append(option.strip())

    if len(options) < 2:

        print(
            "\nA poll must have at least 2 options."
        )

        return

    poll = Poll(
        question,
        options,
        user
    )

    feed.add_post(poll)

    print("\nPoll created!")

    poll.display()


def vote_on_poll(feed):

    if len(feed.posts) == 0:

        print("\nNo posts available.")

        return

    post_id = int(
        input("Enter the Poll Post ID: ")
    )

    for post in feed.posts:

        if post.post_id == post_id:

            if isinstance(post, Poll):

                print("\nPoll:")
                print(post.content)

                print("\nOptions:")

                for i in range(
                    len(post.options)
                ):

                    print(
                        i + 1,
                        ".",
                        post.options[i]
                    )

                choice = int(
                    input("\nEnter your choice: ")
                )

                if (
                    choice >= 1
                    and choice <= len(post.options)
                ):

                    selected_option = (
                        post.options[choice - 1]
                    )

                    post.vote(
                        selected_option
                    )

                    print("\nVote recorded!")

                    post.display()

                else:

                    print("\nInvalid option.")

                return

            else:

                print(
                    "\nThat Post ID is not a poll."
                )

                return

    print("\nPoll not found.")


def like_post(feed):

    if len(feed.posts) == 0:

        print("\nNo posts available.")

        return

    post_id = int(
        input(
            "Enter the Post ID you want to like: "
        )
    )

    for post in feed.posts:

        if post.post_id == post_id:

            post.like()

            print("\nPost liked!")

            print(
                "Total likes:",
                post.likes
            )

            return

    print("\nPost not found.")


def add_comment(feed):

    if len(feed.posts) == 0:

        print("\nNo posts available.")

        return

    post_id = int(
        input(
            "Enter the Post ID you want to comment on: "
        )
    )

    for post in feed.posts:

        if post.post_id == post_id:

            text = input(
                "Enter your comment: "
            )

            post.add_comment(text)

            print("\nComment added!")

            return

    print("\nPost not found.")


def main():

    user = User()

    feed = Feed()

    # Load old data
    load_data(feed)

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            create_confession(
                user,
                feed
            )

            save_data(feed)

        elif choice == "2":

            create_poll(
                user,
                feed
            )

            save_data(feed)

        elif choice == "3":

            feed.display()

        elif choice == "4":

            vote_on_poll(feed)

            save_data(feed)

        elif choice == "5":

            like_post(feed)

            save_data(feed)

        elif choice == "6":

            add_comment(feed)

            save_data(feed)

        elif choice == "7":

            save_data(feed)

            print(
                "Thanks for using VibeCheck!"
            )

            break

        else:

            print(
                "Invalid choice. Please try again."
            )


main()