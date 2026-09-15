def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def update_rating(rating, expected, actual, k=32):
    return rating + k * (actual - expected)


def elo_match(rating_a, rating_b, result_a, k=32):
    expected_a = expected_score(rating_a, rating_b)
    expected_b = 1 - expected_a

    new_a = update_rating(rating_a, expected_a, result_a, k)

    result_b = 1 - result_a
    new_b = update_rating(rating_b, expected_b, result_b, k)

    return new_a, new_b
