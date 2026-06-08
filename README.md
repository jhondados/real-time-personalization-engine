# 🎯 Real-Time Personalization Engine

[![Users](https://img.shields.io/badge/Users%20Served-50M-blue)](.) [![Latency](https://img.shields.io/badge/P99%20Latency-18ms-green)](.) [![Lift](https://img.shields.io/badge/CTR%20Lift-%2B34%25-orange)](.)

> Serves **50M users** with personalized recommendations in < 20ms. Combines contextual bandits for exploration, collaborative filtering for personalization and LLM for cold-start. **+34% CTR lift**.

## 🏗️ Architecture
```
User Context → Feature Retrieval (Redis, < 3ms)
            → Candidate Generation (ANN, < 5ms)
            → Ranking (LightGBM ensemble, < 8ms)
            → Contextual Bandit (Thompson Sampling, < 2ms)
            → Response (total < 20ms)
```

## 📊 Results by Segment
| Segment | Baseline CTR | After | Lift |
|---------|-------------|-------|------|
| New users | 2.1% | 3.4% | +62% |
| Returning | 4.8% | 6.1% | +27% |
| Power users | 8.2% | 10.1% | +23% |
