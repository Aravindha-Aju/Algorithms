# 🧠 Famous Algorithms

> **A journey through the algorithms that shaped computing — and eventually, creating our own.**

This repository is a collection of **famous, interesting, and influential algorithms**, implemented from scratch and explained in a way that's easy to understand.

The goal isn't just to write code.

It's to understand **how the algorithm thinks, why it works, where it came from, and where it's used in the real world.**

---

## 🚀 Why This Repository?

Algorithms are everywhere.

Search engines, social networks, GPS navigation, cryptography, compression, games, artificial intelligence, distributed systems — all of them depend on algorithms.

Some algorithms are simple.

Some are mathematically beautiful.

Some completely changed the world.

This repository is an attempt to explore those algorithms one by one.

```text
Idea
 ↓
Mathematics
 ↓
Algorithm
 ↓
Implementation
 ↓
Real-world application
```

---

# 📚 Algorithms

## ♟️ Ranking & Recommendation

### Elo Rating

A rating algorithm originally developed for chess that estimates the relative strength of players.

**Interesting connection:** Elo-style ranking was famously associated with Mark Zuckerberg's early **FaceMash** project at Harvard.

📁 [`elo-rating/`](./elo-rating/)

---

## 🔍 Searching & Pathfinding

### Binary Search

Efficiently searches a sorted dataset by repeatedly dividing the search space in half.

📁 [`binary-search/`](./binary-search/)

### Dijkstra's Algorithm

Finds the shortest path between nodes in a weighted graph.

📁 [`dijkstra/`](./dijkstra/)

### A* (A-Star)

A pathfinding algorithm that combines actual distance with a heuristic to efficiently search for a destination.

📁 [`astar/`](./astar/)

---

## 🌐 Web & Information

### PageRank

One of the most famous ranking algorithms in computer science.

It helped Google determine the importance of webpages by analyzing the structure of links between them.

> **A page becomes important when important pages link to it.**

📁 [`pagerank/`](./pagerank/)

---

## 🔐 Cryptography

### SHA-256

A cryptographic hash function that converts data into a fixed-size 256-bit hash.

SHA-256 is also heavily associated with Bitcoin's proof-of-work system.

📁 [`sha256/`](./sha256/)

### RSA

One of the foundational public-key cryptographic algorithms.

📁 [`rsa/`](./rsa/)

---

## 🤖 Artificial Intelligence

### Minimax

A decision-making algorithm commonly used for two-player games.

📁 [`minimax/`](./minimax/)

### Alpha-Beta Pruning

An optimization for Minimax that eliminates branches of the game tree that don't need to be explored.

📁 [`alpha-beta-pruning/`](./alpha-beta-pruning/)

---

## 🧬 Genetic Algorithm

An optimization technique inspired by biological evolution.

```text
Population
     ↓
Evaluate
     ↓
Select
     ↓
Crossover
     ↓
Mutation
     ↓
New Generation
     ↺
```

📁 [`genetic-algorithm/`](./genetic-algorithm/)

---

## 📦 Compression

### Huffman Coding

A lossless compression algorithm that assigns shorter binary codes to frequently occurring characters.

📁 [`huffman-coding/`](./huffman-coding/)

---

## 🔤 String Algorithms

### KMP — Knuth-Morris-Pratt

A pattern-searching algorithm that avoids unnecessary comparisons.

📁 [`kmp/`](./kmp/)

### Rabin-Karp

Uses hashing to efficiently search for patterns inside text.

📁 [`rabin-karp/`](./rabin-karp/)

### Boyer-Moore

A powerful string-searching algorithm that can skip large portions of the text.

📁 [`boyer-moore/`](./boyer-moore/)

---

## 🧠 Machine Learning

### K-Means

An unsupervised learning algorithm that groups data into clusters.

📁 [`k-means/`](./k-means/)

### Gradient Descent

An optimization algorithm used to minimize a function and fundamental to training many machine-learning models.

📁 [`gradient-descent/`](./gradient-descent/)

### Backpropagation

The algorithm used to calculate how neural-network parameters should change in response to errors.

📁 [`backpropagation/`](./backpropagation/)

---

## 🌍 Distributed Systems

### Consistent Hashing

Distributes data across servers while minimizing movement when servers are added or removed.

📁 [`consistent-hashing/`](./consistent-hashing/)

### Merkle Tree

A cryptographic tree structure used to efficiently verify large collections of data.

📁 [`merkle-tree/`](./merkle-tree/)

### Raft

A consensus algorithm that helps distributed systems agree on a shared state.

📁 [`raft/`](./raft/)

---

## ₿ Blockchain & Bitcoin

### Proof of Work

A computational mechanism used by Bitcoin to make adding new blocks expensive.

📁 [`proof-of-work/`](./proof-of-work/)

---

# 🗂️ Repository Structure

Every algorithm follows a similar structure:

```text
algorithm-name/
│
├── README.md
├── implementation.py
└── test.py
```

Each algorithm's README will explain:

* 🧠 What it does
* 📜 History and origin
* ⚙️ How it works
* 📐 Mathematics
* 💻 Implementation
* ⏱️ Time complexity
* 💾 Space complexity
* 🌎 Real-world applications
* 💡 Interesting facts

---

# 🎯 The Long-Term Goal

Learning famous algorithms is only the beginning.

Eventually, we want to go from:

```text
Understanding algorithms
        ↓
Implementing algorithms
        ↓
Modifying algorithms
        ↓
Combining ideas
        ↓
Experimenting
        ↓
❓ What if we created our own?
        ↓
🧠 OUR OWN ALGORITHMS
```

One day, this repository won't just contain algorithms created by other people.

**We'll create our own.**

We'll take problems we encounter, research existing solutions, understand the mathematics behind them, experiment with different approaches, and eventually try to design algorithms of our own.

They might be terrible at first.

They might be inefficient.

They might completely fail.

That's okay.

Because the goal isn't to immediately invent the next PageRank or SHA-256.

The goal is to learn **how algorithmic ideas are born.**

> **First, we learn the algorithms that changed the world.
> Then, we try to create something that changes it ourselves.**

---

# 🛠️ Languages

Primary language:

```text
Python
```

More languages may be added later:

```text
C
C++
Java
JavaScript
Rust
```

The focus is on understanding the **algorithm itself**, rather than relying on built-in implementations.

---

# 📈 Learning Progress

| Category               | Status        |
| ---------------------- | ------------- |
| Searching              | 🟡            |
| Sorting                | ⚪             |
| Graphs                 | 🟡            |
| Ranking                | 🟢            |
| Cryptography           | 🟡            |
| AI                     | 🟡            |
| Machine Learning       | 🟡            |
| Compression            | 🟡            |
| Distributed Systems    | 🟡            |
| Blockchain             | 🟡            |
| **Our Own Algorithms** | 🔮 **Future** |

**Legend**

🟢 Completed
🟡 In Progress
⚪ Planned
🔮 Future Goal

---

# 🔥 The Bigger Picture

Algorithms aren't just pieces of code.

They are ideas.

**Elo** turns competitions into rankings.

**PageRank** turns hyperlinks into search relevance.

**A*** turns maps into paths.

**SHA-256** turns data into cryptographic fingerprints.

**Genetic Algorithms** turn evolution into optimization.

**Minimax** turns game strategy into computation.

**Raft** turns distributed machines into a coordinated system.

And eventually...

**We want to turn our own ideas into algorithms.**

---

# ⭐ Mission

```text
LEARN
  ↓
UNDERSTAND
  ↓
BUILD
  ↓
EXPERIMENT
  ↓
CREATE
```

> **Learn what others built.
> Understand why it works.
> Build it yourself.
> Then create something new.**

---

## 📌 Currently Exploring

```text
♟️ Elo Rating
```

More algorithms coming soon.

---

### 🧑‍💻 Author

**Aju**

Learning algorithms by building them from scratch.

> *"The best way to understand an algorithm is to build it."*
