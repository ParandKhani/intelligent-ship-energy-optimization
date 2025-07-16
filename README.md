# Intelligent Ship Energy Optimization 🚢⚡

This project presents a simplified Digital Twin model to simulate and optimize energy consumption in intelligent ships.

### 🔍 Project Summary

We modeled three main onboard systems:

- **Main Engine** — energy depends quadratically on speed (v)
- **Air Conditioning (AC)** — active when temperature > 20°C
- **Electrical Load** — energy proportional to usage time (h)

A simple Python model calculates total daily energy consumption.  
We tested 5 scenarios and performed an exhaustive parameter optimization  
to find the most energy-efficient configuration.

### 📈 Features

- Mathematical modeling of onboard systems  
- Parametric simulation with Python  
- Scenario-based energy analysis  
- Simple optimization algorithm  
- IEEE-style scientific article included

### 🛠 Technologies

- Python 3.x  
- Matplotlib  
- Numpy

### 📄 Files Included

- `energy_model.py`: main Python script  
- `scenarios_results.png`: bar chart of energy consumption in 5 scenarios  
- `optimization_summary.txt`: best configuration found (v=10, T=18, h=5)

---

### 🔗 Author

Parand Khani — PhD Student @ University of Messina  
Feel free to use or extend this work with citation.
