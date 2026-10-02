\# Facemash Ranking Algorithm



A Python implementation of a pairwise ranking system inspired by \*\*Facemash\*\*, the website associated with Mark Zuckerberg's early Harvard project and portrayed in the 2010 film \*\*\*The Social Network\*\*\*.



The project explores the algorithmic idea behind comparing two entities at a time, collecting the comparison results, and using those results to construct a relative ranking.



> \*\*Note:\*\* This repository is a modern technical reconstruction. It is not the original Facemash source code.



\---



\## Background



\*\*Facemash\*\* was created by Mark Zuckerberg while he was a student at Harvard University in 2003.



The basic concept was to present users with photographs of two Harvard students and allow them to choose between them. The system then used the accumulated choices to produce rankings.



The project became part of the early history surrounding what would eventually become Facebook.



Facemash was also prominently portrayed in the 2010 film \*\*\*The Social Network\*\*\*, which dramatizes the creation of the site and its role in the story of Facebook's origins.



The movie presents the project as a rapidly developed website that used student photographs and a ranking mechanism to determine comparative results.



\---



\## The Algorithmic Concept



The central idea can be represented as:



```text

Two Entities

&#x20;    │

&#x20;    ▼

User Comparison

&#x20;    │

&#x20;    ▼

Winner / Loser

&#x20;    │

&#x20;    ▼

Rating Update

&#x20;    │

&#x20;    ▼

Updated Rankings

```



Rather than assigning an absolute score directly, the system builds a \*\*relative ranking through repeated pairwise comparisons\*\*.



\---



\## Modern Reconstruction



This implementation uses an \*\*Elo-style rating system\*\* to model the ranking mechanism.



Each entity begins with:



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



After a comparison, the ratings are updated:



```text

RA' = RA + K(SA - EA)



RB' = RB + K(SB - EB)

```



Where:



```text

RA = Rating of A

RB = Rating of B

SA = Actual score of A

SB = Actual score of B

EA = Expected score of A

EB = Expected score of B

K  = Rating adjustment factor

```



\---



\## System Workflow



```text

&#x20;                   FACEMASH

&#x20;                      │

&#x20;                      ▼

&#x20;              Select Two People

&#x20;                      │

&#x20;                      ▼

&#x20;                Display Pair

&#x20;                      │

&#x20;                      ▼

&#x20;               User Selection

&#x20;                      │

&#x20;                      ▼

&#x20;             Calculate Probability

&#x20;                      │

&#x20;                      ▼

&#x20;                Update Ratings

&#x20;                      │

&#x20;                      ▼

&#x20;               Store New Ratings

&#x20;                      │

&#x20;                      ▼

&#x20;               Select Next Pair

&#x20;                      │

&#x20;                      ▼

&#x20;                    Repeat

&#x20;                      │

&#x20;                      ▼

&#x20;                Sort Ratings

&#x20;                      │

&#x20;                      ▼

&#x20;                 Final Ranking

```



\---



\## Project Structure



```text

facemash-ranking/

│

├── ranking.py

└── README.md

```



\## Requirements



\* Python 3.8+

\* Python Standard Library

\* No external dependencies



\## Core Components



\### `RankingSystem`



Maintains entity ratings and manages the ranking process.



\### `expected\_score()`



Calculates the expected result of a comparison based on current ratings.



\### `update()`



Adjusts the ratings of both participants after a comparison.



\### `select\_pair()`



Selects two distinct entities for comparison.



\### `get\_ranking()`



Returns all entities ordered by their current rating.



\---



\## Web Application Architecture



The ranking engine can be integrated into a complete web application:



```text

&#x20;               WEB APPLICATION

&#x20;                      │

&#x20;       ┌──────────────┴──────────────┐

&#x20;       │                             │

&#x20;   Frontend                       Backend

&#x20;       │                             │

&#x20;HTML / CSS / JS                 Python API

&#x20;                                     │

&#x20;                                     ▼

&#x20;                             Ranking Engine

&#x20;                                     │

&#x20;                                     ▼

&#x20;                                 Database

```



The frontend handles:



\* User interface

\* Photograph presentation

\* User selection

\* Navigation



The backend handles:



\* Pair selection

\* Comparison processing

\* Rating calculations

\* Ranking generation

\* Data persistence



\---



\## Possible API Structure



```text

GET  /entities

GET  /pair

POST /comparison

GET  /ranking

```



A frontend can submit a comparison to the backend, after which the backend updates the ratings and returns the next pair.



\---



\## Historical Context



Facemash is significant because it demonstrates an early example of turning a simple social interaction into a computational ranking system.



The concept can be reduced to:



```text

Human Choice

&#x20;    ↓

Data

&#x20;    ↓

Algorithm

&#x20;    ↓

Ranking

```



This same general pattern appears in many modern systems, including recommendation systems, competitive rankings, search relevance, and preference-learning systems.



However, the implementation in this repository should \*\*not be interpreted as the verified original Facemash algorithm\*\*. The original source code is not publicly available, and the Elo-style mechanism used here is a modern reconstruction for educational purposes.



\---



\## Relation to The Social Network



The 2010 film \*\*\*The Social Network\*\*\* dramatizes the development of Facemash and presents it as an important early event in Mark Zuckerberg's story.



The film focuses on the rapid development of the website, the use of Harvard student photographs, the site's sudden popularity, and the consequences that followed.



The implementation in this repository takes the \*\*algorithmic concept portrayed in the film\*\* and reconstructs it as a standalone Python ranking engine.



\---



\## Future Development



Possible extensions include:



\* Web interface

\* User authentication

\* Image storage

\* Persistent database

\* REST API

\* Pair-selection optimization

\* Rating history

\* Ranking analytics

\* Match statistics

\* Administrative dashboard



\---



\## Disclaimer



This project is an \*\*educational reconstruction inspired by Facemash and its depiction in \*The Social Network\*\*\*.



It does not contain the original Facemash source code and does not claim to reproduce its exact historical implementation.



The system is intended for experimentation with pairwise ranking algorithms and web application architecture.



\## License



This project is intended for educational and experimental purposes.



