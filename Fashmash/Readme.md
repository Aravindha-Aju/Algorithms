# Facemash — Ranking Algorithm

A Python reconstruction of the **pairwise ranking concept behind Facemash**, the 2003 Harvard website associated with Mark Zuckerberg and later portrayed in the 2010 film ***The Social Network***.

The project explores how a simple comparison between two people can be converted into a dynamic numerical ranking through repeated user selections.

> **Note:** This is a modern educational reconstruction. It is not the original Facemash source code or a claim about its exact historical ranking implementation.

---

## Background

Facemash was created by Mark Zuckerberg while studying at Harvard University in 2003. The website presented users with two photographs and allowed them to choose between them.

The accumulated choices were used to create a relative ranking.

Facemash was later dramatized in ***The Social Network (2010)***, where its creation and rapid popularity form an important part of the opening story.

From an algorithmic perspective, the interesting idea is:

```text
Two People
    |
    v
User Choice
    |
    v
Rating Update
    |
    v
Updated Ranking
    |
    v
Repeat
```

---

## Core Concept

The system uses **pairwise comparison**.

Instead of asking a user to assign an absolute score, the system presents two entities:

```text
Person A

   VS

Person B
```

The user selects one.

That result is then used to update the ratings of both participants.

After many comparisons, the ratings are sorted to produce a ranking.

```text
Comparison
     |
     v
Winner / Loser
     |
     v
Rating Calculation
     |
     v
Rating Update
     |
     v
Ranking
```

---

## Ranking Model

This implementation uses an **Elo-style rating system** as a modern reconstruction of the pairwise ranking concept.

Every entity begins with:

```text
Initial Rating = 1500
```

For two entities `A` and `B`, the expected score of `A` is:

```text
EA = 1 / (1 + 10^((RB - RA) / 400))
```

The expected score of `B` is:

```text
EB = 1 - EA
```

After a comparison, the ratings are updated using:

```text
RA' = RA + K(SA - EA)

RB' = RB + K(SB - EB)
```

Where:

```text
RA, RB = Current ratings
SA, SB = Actual results
EA, EB = Expected results
K      = Rating adjustment factor
```

The implementation uses:

```text
K = 32
```

A result that is less expected produces a larger rating change, while an expected result produces a smaller change.

---

## Algorithm

```text
INITIALIZE

Assign every entity a rating of 1500.

REPEAT

    Select two different entities.

    Display both entities.

    Receive the user's selection.

    Calculate expected scores.

    Determine actual scores.

    Calculate rating changes.

    Update both ratings.

    Store the updated ratings.

UNTIL

    Ranking process is stopped.

OUTPUT

    Sort all entities by rating in descending order.
```

---

## System Workflow

```text
                    FACEMASH
                       |
                       v
              Initialize Ratings
                       |
                       v
              Select Two People
                       |
                       v
                  Display Pair
                       |
                       v
                 User Selection
                       |
                       v
              Calculate Expected
                    Scores
                       |
                       v
                 Update Ratings
                       |
                       v
                Store Results
                       |
                       v
               Select Next Pair
                       |
                       v
                     Repeat
                       |
                       v
                Sort By Rating
                       |
                       v
                 Final Ranking
```

---

## Python Implementation

The ranking engine is implemented in Python using an object-oriented design.

```python
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
        return random.sample(
            list(self.ratings.keys()),
            2
        )

    def get_ranking(self):
        return sorted(
            self.ratings.items(),
            key=lambda item: item[1],
            reverse=True
        )
```

---

## Implementation Structure

The project currently contains:

```text
Facemash/
│
├── ranking.py
└── README.md
```

The `RankingSystem` is responsible for:

- Initializing ratings
- Selecting comparison pairs
- Calculating expected scores
- Updating ratings
- Generating rankings

The ranking engine is intentionally independent from the web interface.

---

## Architecture

A complete web implementation can be structured as:

```text
                     WEB BROWSER
                          |
                          v
                 HTML / CSS / JS
                          |
                          v
                     PYTHON API
                          |
                          v
                   RANKING ENGINE
                          |
                          v
                      DATABASE
```

### Frontend

Responsible for:

- Displaying the two photographs
- Receiving the user's selection
- Requesting the next comparison
- Displaying rankings

### Backend

Responsible for:

- Selecting pairs
- Processing comparisons
- Calculating rating changes
- Updating rankings
- Communicating with the database

### Database

Responsible for storing:

- Entities
- Images
- Ratings
- Comparison history

---

## Possible API

A web version could expose endpoints such as:

```text
GET  /entities
GET  /pair
POST /comparison
GET  /ranking
```

The comparison flow would be:

```text
Browser
   |
   | GET /pair
   v
Backend
   |
   v
Return Two Entities
   |
   v
User Makes Selection
   |
   | POST /comparison
   v
Backend
   |
   v
Update Ratings
   |
   v
Database
   |
   v
Next Comparison
```

---

## Technology Stack

```text
Language       Python

Ranking        Elo-style Pairwise Rating

Frontend       HTML
               CSS
               JavaScript

Backend        Python API

Database       PostgreSQL / MySQL
```

The current implementation focuses on the Python ranking engine.

---

## Complexity

For `n` entities:

```text
Pair Selection       O(1)
Rating Update        O(1)
Ranking Generation   O(n log n)
```

The rating update only affects the two entities involved in the current comparison.

The complete ranking requires sorting the current ratings.

---

## Historical Accuracy

The original Facemash source code and its exact internal ranking algorithm are not reproduced in this project.

The **Elo-style model is a modern reconstruction** used to demonstrate how a pairwise comparison system can maintain dynamic ratings.

Therefore, the relationship is:

```text
Historical Facemash
        |
        v
Pairwise Comparison Concept
        |
        v
Modern Elo-style Model
        |
        v
Python Implementation
```

The implementation should not be interpreted as verified original Facemash source code.

---

## Why This Project?

Facemash is an interesting example of how a very simple interaction can become an algorithmic system:

```text
Human Preference
       |
       v
Collected Data
       |
       v
Mathematical Model
       |
       v
Rating
       |
       v
Ranking
```

The same fundamental idea of converting comparisons and preferences into numerical rankings appears in many modern computational systems.

---

## Future Development

Possible extensions include:

- Web interface
- Persistent database
- REST API
- Image management
- Rating history
- Comparison analytics
- Improved pair selection
- Ranking visualization
- User authentication

---

## Disclaimer

This project is an **independent educational reconstruction inspired by Facemash and its depiction in *The Social Network*.**

It does not contain the original Facemash source code and does not claim to reproduce its exact historical implementation.

The purpose of this project is to study:

- Pairwise ranking
- Rating algorithms
- Probability
- Python
- Backend architecture
- Algorithmic systems

---

## License

This project is intended for educational and experimental purposes.
