
import matplotlib.pyplot as plt

def energy_consumption(v, T, h):
    E_motor = 0.2 * (v ** 2)
    E_AC = 1.5 * max(0, T - 20)
    E_electric = 0.5 * h
    total_energy = E_motor + E_AC + E_electric
    return total_energy

scenarios = [(10, 22, 6), (15, 28, 10), (18, 25, 12), (20, 30, 8), (12, 18, 5)]
totals = [energy_consumption(v, T, h) for v, T, h in scenarios]
labels = [f"Scenario {i+1}" for i in range(len(scenarios))]

plt.figure(figsize=(6,4))
plt.bar(labels, totals, color='skyblue')
plt.title("Total Energy Consumption per Scenario")
plt.ylabel("Energy Units")
plt.xticks(rotation=30)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("scenarios_results.png")

best_energy = float('inf')
best_config = None
for v in range(10, 21):
    for T in range(18, 31):
        for h in range(5, 13):
            e = energy_consumption(v, T, h)
            if e < best_energy:
                best_energy = e
                best_config = (v, T, h)

with open("optimization_summary.txt", "w") as f:
    f.write(f"Best Configuration:\n")
    f.write(f"Speed (v): {best_config[0]} km/h\n")
    f.write(f"Temperature (T): {best_config[1]} °C\n")
    f.write(f"Electric hours (h): {best_config[2]} hrs\n")
    f.write(f"Total Energy: {best_energy} units\n")
