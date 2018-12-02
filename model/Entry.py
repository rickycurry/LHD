class Entry:
    upvotes = 0
    downvotes = 0

    def __init__(self, demo):
        self.demo = demo

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes =+1