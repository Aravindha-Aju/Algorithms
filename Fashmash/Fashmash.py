import random

INITIAL_RATING = 1500
K_FACTOR = 32


class RankingSystem:

    def __init__(self, entities):
        self.ratings = {
            entity: INITIAL_RATING
            for entity in entities
        }

    @staticmethod
    def expected_score(rating_a, rating_b):
        return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

    def update(self, winner, loser):
        rating_winner = self.ratings[winner]
        rating_loser = self.ratings[loser]

        expected_winner = self.expected_score(
            rating_winner,
            rating_loser
        )

        expected_loser = 1 - expected_winner

        self.ratings[winner] = (
            rating_winner
            + K_FACTOR * (1 - expected_winner)
        )

        self.ratings[loser] = (
            rating_loser
            + K_FACTOR * (0 - expected_loser)
        )

    def select_pair(self):
        return random.sample(list(self.ratings.keys()), 2)

    def get_ranking(self):
        return sorted(
            self.ratings.items(),
            key=lambda item: item[1],
            reverse=True
        )