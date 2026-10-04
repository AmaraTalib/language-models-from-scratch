from string import punctuation
from collections import Counter

post_comments_with_labels = [
    ("I love this post.", "pos"),
    ("This post is your best work.", "pos"),
    ("I really liked this post.", "pos"),
    ("I agree 100 percent. This is true", "pos"),
    ("This post is spot on!", "pos"),
    ("So smart!", "pos"),
    ("What a good point!", "pos"),
    ("Bad stuff.", "neg"),
    ("I hate this.", "neg"),
    ("This post is horrible.", "neg"),
    ("I really disliked this post.", "neg"),
    ("What a waste of time.", "neg"),
    ("I do not agree with this post.", "neg"),
    ("I can't believe you would post this.", "neg"),
]


class NaiveBayesClassifier:
    def __init__(self, samples):
        self.mapping = {"pos": [], "neg": []}
        self.sample_count = len(samples)

        for text, label in samples:
            self.mapping[label] += self.tokenize(text)

        self.pos_counter = Counter(self.mapping["pos"])
        self.neg_counter = Counter(self.mapping["neg"])

    @staticmethod
    def tokenize(text):
        return (
            text.lower()
            .translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def classify(self, text):
        tokens = self.tokenize(text)

        pos = 1
        neg = 1

        for token in tokens:
            pos *= self.pos_counter[token] / len(self.mapping["pos"])
            neg *= self.neg_counter[token] / len(self.mapping["neg"])

        if pos > neg:
            return "pos"
        else:
            return "neg"


cl = NaiveBayesClassifier(post_comments_with_labels)


def get_sentiment(text):
    return cl.classify(text)


print(get_sentiment("I love this post"))
print(get_sentiment("This post is horrible"))