import matplotlib.pyplot as plt

horas = list(range(51))

costos_A = [0] * 51
costos_B = [0] * 51
costos_C = [0] * 51

for x in range(51):
    costos_A[x] = 40 * x + 200
    costos_B[x] = 70 * x + 50
    costos_C[x] = -2 * (x * x) + 80 * x + 100

plt.figure(figsize=(10, 6))
plt.title('Comparación de Costos de Desarrollo por Plan', fontsize=14)
plt.xlabel('Cantidad de Horas Mensuales (x)', fontsize=12)
plt.ylabel('Costo Mensual ($)', fontsize=12)

plt.plot(horas, costos_A, label='Plan A (40x + 200)', color='blue', linewidth=2)
plt.plot(horas, costos_B, label='Plan B (70x + 50)', color='orange', linewidth=2)
plt.plot(horas, costos_C, label='Plan C (-2x² + 80x + 100)', color='green', linewidth=2)

plt.scatter(5, 400, color='red', s=100, zorder=5, label='Intersección A-B (5h, $400)')
plt.scatter(20, 900, color='purple', s=100, zorder=5, label='Vértice de C (20h, $900)')

plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()