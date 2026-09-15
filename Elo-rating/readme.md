# ♟️ Elo Rating Algorithm

> **How a chess ranking algorithm helped inspire one of the earliest ideas behind Facebook.**

## 🧠 What is Elo?

The **Elo Rating System** is a mathematical ranking algorithm originally developed for chess.

Instead of simply counting wins and losses, Elo estimates **how likely one player is to beat another** based on their ratings.

The interesting idea is:

> **Beating someone stronger should be worth more than beating someone weaker.**

---

## 👀 The Interesting Story

Before Facebook, **Mark Zuckerberg** created a Harvard website called **FaceMash**.

The basic idea was simple:

> Show two students' photos and let users choose which person they considered more attractive.

But there was a problem:

### How do you rank thousands of people?

You can't manually create a ranking.

Instead, you can treat every comparison like a competition.

```text
Person A vs Person B
        ↓
    User chooses
        ↓
   A wins / B wins
        ↓
   Update ratings
        ↓
     New ranking
```

This is where the **Elo-style rating concept** becomes interesting.

Each person can start with a rating:

```text
Alice   → 1500
Bob     → 1500
Charlie → 1500
```

After enough comparisons, the system naturally produces a ranking.

> **Note:** FaceMash is widely described as using an Elo-style ranking system, but the exact original implementation is not publicly documented well enough to say it was identical to the standard chess Elo formula.

---

# ⚙️ How Elo Works

Suppose:

```text
Player A = 1600
Player B = 1400
```

The algorithm expects A to win more often because A has a higher rating.

The expected score is:

$$
E_A = \frac{1}{1 + 10^{(R_B-R_A)/400}}
$$

For these ratings:

```text
Expected score of A ≈ 0.76
Expected score of B ≈ 0.24
```

So the algorithm expects A to win roughly **76%** of the time.

---

# 🔄 Updating the Rating

After the match, Elo updates the rating using:

$$
R' = R + K(S-E)
$$

Where:

| Symbol | Meaning                  |
| ------ | ------------------------ |
| `R`    | Current rating           |
| `R'`   | New rating               |
| `K`    | Rating adjustment factor |
| `S`    | Actual result            |
| `E`    | Expected result          |

For example:

```text
A = 1600
B = 1400

A wins

Expected A = 0.76
Actual A   = 1
K          = 32
```

Therefore:

$$
R'_A = 1600 + 32(1-0.76)
$$

```text
A ≈ 1608
```

A gains rating because the result was expected.

---

# 🤯 But What If B Wins?

This is where Elo becomes really interesting.

```text
A = 1600
B = 1400
```

Everyone expects A to win.

But B wins.

The algorithm basically says:

> **Whoa. That was unexpected.**

So B receives a much larger rating increase.

```text
A → loses rating
B → gains rating
```

The more surprising the result, the larger the rating change.

---

# 💻 Implementation

```python
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
```

Example:

```python
a, b = elo_match(1600, 1400, 1)

print(a)
print(b)
```

---

# 🌎 Where Elo Can Be Used

Elo isn't limited to chess.

The same underlying idea can be useful whenever entities are repeatedly compared:

* ♟️ Chess
* 🎮 Competitive games
* 🏆 Sports
* 👥 Ranking systems
* 🤖 AI competitions
* 📊 Recommendation/ranking experiments
* 🗳️ Pairwise preference systems

---

# 💡 The Big Idea

Elo demonstrates a powerful concept:

```text
Competition
     ↓
Expected outcome
     ↓
Actual outcome
     ↓
Difference
     ↓
Rating adjustment
     ↓
Better ranking
```

Instead of asking:

> **"Who is #1?"**

Elo asks:

> **"Given what we currently know, how strong is each participant?"**

And every new competition gives the system more information.

---

## 🚀 Why I Added This Algorithm

This isn't just another algorithm implementation.

It connects:

**Chess → Mathematics → Ranking Systems → FaceMash → Social Platforms**

A relatively simple equation can turn thousands of individual comparisons into a continuously evolving ranking system.

**That's what makes Elo interesting.**

