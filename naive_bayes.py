from collections import defaultdict
import math
class MultinomialNB:
    def __init__(self, articles_per_tag):
        # Don't change the following two lines of code.
        self.articles_per_tag = articles_per_tag  # See question prompt for details.
        self.train()

    def train(self):
        # We need to make a list of priors, a list of probabilities for each word respective to each
        # class.
        # Getting the vocabulary and the vocabulary count for every word respective to the tags
        self.prior_per_tag = {}
        self.word_occurences_per_tag = defaultdict(lambda: {tag: 0 for tag in self.articles_per_tag.keys()})
        self.total_words_per_tag = defaultdict(lambda: 0)
        total_articles = 0
        for tag in self.articles_per_tag:
            for article in self.articles_per_tag[tag]:
                total_articles += 1
                for word in article:
                    self.word_occurences_per_tag[word][tag] += 1
                    self.total_words_per_tag[tag] += 1

        # Getting the probabilities for each of the words in each tag
        self.word_probabilities_per_tag = defaultdict(lambda: {tag: .50 for tag in self.articles_per_tag.keys()})
        for word, tag_map in self.word_occurences_per_tag.items():
            for tag in tag_map.keys():
                self.word_probabilities_per_tag[word][tag] = (self.word_occurences_per_tag[word][tag]+1) / (
                self.total_words_per_tag[tag]+2)
        print(self.word_probabilities_per_tag)

        # Getting the priors for eajjkch tag
        for tag in self.articles_per_tag:
            self.prior_per_tag[tag] = len(self.articles_per_tag[tag])/total_articles


    def predict(self, article):
        # We need to get the probability of each word being each tag along with every other
        # word NOT being in a document per tag
        word_count_per_word = defaultdict(lambda: 0)

        # Getting the frequency of each word for the powers in the numerator
        for word in article:
            word_count_per_word[word] += 1 

        # Getting the probabilities of all possible classes
        tag_probabilities = defaultdict(int)
        numerator = 0
        #denominator = 0
        for tag in self.articles_per_tag:
            tag_probabilities[tag] += math.log(self.prior_per_tag[tag])
            for word in article:
                # Adding the posterior to the tag probability
                tag_probabilities[tag] += math.log(self.word_probabilities_per_tag[word][tag])#**word_count_per_word[word]
                # We use the proportional value rather than the actual percentage for whatever reason
                # We also don't use the denominator even though it says probability
                # denominator += math.log(self.word_probabilities_per_tag[word][tag])

        return tag_probabilities
