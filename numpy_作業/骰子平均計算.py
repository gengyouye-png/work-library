import numpy as np


def simulate_dice(seed, times=10000):
    rng = np.random.default_rng(seed)
    rolls = rng.integers(1, 7, size=times)
    counts = np.bincount(rolls, minlength=7)[1:]
    proportions = counts / times
    theoretical = 1 / 6
    differences = proportions - theoretical

    return rolls, counts, proportions, differences


def print_result(seed, counts, proportions, differences):
    print(f"seed = {seed}")
    print("點數  出現次數  出現比例  與理論值 1/6 的差")

    for point in range(1, 7):
        print(
            f"{point:>2}    "
            f"{counts[point - 1]:>5}    "
            f"{proportions[point - 1]:.4f}    "
            f"{differences[point - 1]:+.4f}"
        )

    print(f"比例總和: {proportions.sum():.4f}")
    print()


times = 10000
theoretical = 1 / 6
seeds = [1422697, 2026, 31]

print("作業一：骰子平均計算")
print(f"模擬擲骰子 {times:,} 次")
print(f"理論上每個點數出現比例為 {theoretical:.4f}")
print()

for seed in seeds:
    rolls, counts, proportions, differences = simulate_dice(seed, times)
    print_result(seed, counts, proportions, differences)


