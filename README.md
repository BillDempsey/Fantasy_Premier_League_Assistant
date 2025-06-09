# Fantasy Premier League Player Stats Analyzer

This is a Python script that returns statistics for Fantasy Premier League (FPL) players over the past number of years. It calculates:

- **PPG (Points Per Game)** – a measure of player productivity
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

1. **Evaluating Optimality**  
   Determine whether this current strategy is actually optimal, using more rigorous data-driven methods.

2. **Fixture-Aware Cost Effectiveness**  
   Build an algorithm to evaluate how upcoming fixtures affect the cost-effectiveness of each player — adjusting PPGPE dynamically based on opponent difficulty and other factors.

---

## ▶How to Use

### Requirements

- Python 3.7 or higher
- Dependencies listed in `requirements.txt`

Install dependencies with:

```bash
pip install -r requirements.txt
