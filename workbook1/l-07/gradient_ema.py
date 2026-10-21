import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# 1. Генерация данных
# ============================================================

rng = np.random.default_rng(42)

N = 10

mean = 1.0
variance = 0.5
std = np.sqrt(variance)

gradients = rng.normal(loc=mean, scale=std, size=N)

honest_mean = np.mean(gradients)

print("Градиенты:\n", gradients)

print()
print("Честное полное среднее:\n", honest_mean)

# ============================================================
# 2. TODO: реализовать EMA по эпохам
# ============================================================

def run_ema_epochs(values, beta, epochs):
    """
    Запускает EMA по одному и тому же конечному набору
    градиентов на протяжении нескольких эпох.

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
# 3. Запуск эксперимента
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

    plt.plot(epoch_numbers, errors, label=f"beta={beta}")

    print()
    print("beta =", beta)
    print("Финальное значение EMA:", x_values[-1])
    print("Финальная абсолютная ошибка:", errors[-1])

plt.xlabel("Эпоха s")
plt.ylabel("|x_s - honest_mean|")
plt.title("Ошибка EMA в конце эпохи")
plt.legend()
plt.grid(True)
plt.show()

# ============================================================
# 4. Опционально: построить график с лог. шкалой по оси y
# ============================================================

plt.figure(figsize=(9, 5))

for beta in betas:
    x_values = run_ema_epochs(
        values=gradients,
        beta=beta,
        epochs=epochs,
    )

    errors = np.abs(x_values - honest_mean)

    plt.semilogy(epoch_numbers, errors, label=f"beta={beta}")

plt.xlabel("Эпоха s")
plt.ylabel("|x_s - honest_mean|")
plt.title("Ошибка EMA в конце эпохи лог. масштаб")
plt.legend()
plt.grid(True)
plt.show()
