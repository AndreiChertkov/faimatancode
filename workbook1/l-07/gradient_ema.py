import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# 1. Data generation
# ============================================================

rng = np.random.default_rng(42)

N = 10

mean = 1.0
variance = 0.5
std = np.sqrt(variance)

gradients = rng.normal(loc=mean, scale=std, size=N)

honest_mean = np.mean(gradients)

print("Gradients:")
print(gradients)

print()
print("Honest full mean:")
print(honest_mean)


# ============================================================
# 2. TODO: implement EMA over epochs
# ============================================================

def run_ema_epochs(values, beta, epochs):
    """
    Запускает EMA по одному и тому же конечному набору градиентов
    на протяжении нескольких эпох.

    Параметры:
    values -- массив градиентов G_1, ..., G_N;
    beta   -- параметр EMA;
    epochs -- число полных проходов по values.

    Возвращает:
    numpy-массив [x_0, x_1, ..., x_epochs],
    где x_s -- значение EMA в конце эпохи s.
    """
    # TODO: реализуйте функцию

    # Подсказка:
    # - выберите начальное значение EMA перед первой эпохой;
    # - сохраните его как x_0;
    # - на каждой эпохе пройдите по всем градиентам в values;
    # - после каждой полной эпохи добавьте текущее значение EMA.

    pass


# ============================================================
# 3. Run experiment
# ============================================================

betas = [0.1, 0.9, 0.99]
epochs = 10000

epoch_numbers = np.arange(0, epochs + 1)

plt.figure(figsize=(9, 5))

for beta in betas:
    x_values = run_ema_epochs(
        values=gradients,
        beta=beta,
        epochs=epochs,
    )

    errors = np.abs(x_values - honest_mean)

    plt.plot(
        epoch_numbers,
        errors,
        label=f"beta={beta}",
    )

    print()
    print("beta =", beta)
    print("Final EMA value:", x_values[-1])
    print("Final absolute error:", errors[-1])

plt.xlabel("epoch s")
plt.ylabel("|x_s - honest_mean|")
plt.title("EMA end-of-epoch error")
plt.legend()
plt.grid(True)
plt.show()


# ============================================================
# 4. Optional: plot on logarithmic y-scale
# ============================================================

plt.figure(figsize=(9, 5))

for beta in betas:
    x_values = run_ema_epochs(
        values=gradients,
        beta=beta,
        epochs=epochs,
    )

    errors = np.abs(x_values - honest_mean)

    plt.semilogy(
        epoch_numbers,
        errors,
        label=f"beta={beta}",
    )

plt.xlabel("epoch s")
plt.ylabel("|x_s - honest_mean|")
plt.title("EMA end-of-epoch error, logarithmic scale")
plt.legend()
plt.grid(True)
plt.show()
