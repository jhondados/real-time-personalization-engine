"""Real-time personalization ranker."""
import numpy as np
from scipy.stats import beta
from typing import List, Tuple

class ThompsonSamplingBandit:
    """Contextual bandit with Thompson Sampling for exploration."""
    def __init__(self, n_arms: int):
        self.alpha = np.ones(n_arms)  # successes + 1
        self.beta_  = np.ones(n_arms)  # failures + 1

    def select_arm(self) -> int:
        samples = [beta.rvs(a, b) for a, b in zip(self.alpha, self.beta_)]
        return int(np.argmax(samples))

    def update(self, arm: int, reward: float):
        self.alpha[arm] += reward
        self.beta_[arm]  += (1 - reward)

class PersonalizationRanker:
    def __init__(self, n_items: int):
        self.bandit = ThompsonSamplingBandit(n_items)

    def rank(self, user_embedding: np.ndarray, item_embeddings: np.ndarray,
             context: dict = None) -> List[int]:
        scores = item_embeddings @ user_embedding
        base_ranking = np.argsort(scores)[::-1].tolist()
        # Apply bandit exploration for top-K
        top_k = base_ranking[:20]
        explore_arm = self.bandit.select_arm()
        if explore_arm not in top_k:
            top_k[19] = explore_arm  # inject exploration
        return top_k
