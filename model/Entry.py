class Entry(object):

    def __init__(self, url, transcript, up, down):
        self.url = url
        self.transcript = transcript
        self.up = up
        self.down = down

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes =+1