# Fantasy Premier League Player Stats Analyzer

This is a Python script that returns statistics for Fantasy Premier League (FPL) players over the past number of years. It calculates:

- **PPG (Points Per Game)** – simplest measure of player performance, taking games missed into account
- **PPGPE (Points Per Game Per Euro)** – a custom metric to evaluate the cost-effectiveness of each player

The goal is to help inform team selection based on both performance and value.

---

## Current Strategy

The current strategy is based on a combination of heuristics and intuition. The approach is to:

- Pick **two big-name players**
- Fill out the rest of the squad with **cost-effective** players (i.e., high PPGPE)

This allows for a balance between premium performers and good value picks across the squad.

---

## Future Work

Planned improvements include:

1. Determine whether this current strategy is actually optimal, using Monte Carlo analysis... will first need to build framework for points scoring system etc.

2. Build an algorithm to evaluate how upcoming fixtures affect the cost-effectiveness of each player 

3. FOR NOW- UPLOAD VERSION OF CODE WITH GUI TO GIT REPOSITORY
