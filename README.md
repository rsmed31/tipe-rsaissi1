# Traffic Optimization Using Ant Colony Optimization (ACO)

This project explores how ant colony optimization (ACO) algorithms can be used to regulate traffic flow in urban intersections. Through mathematical modeling, Python simulations, and traffic simulators (SUMO + PLEXE), the system aims to reduce vehicle waiting times and emissions.

## 🧠 Objective

Design and evaluate a bio-inspired traffic light control system using ACO to:
- Minimize traffic congestion
- Reduce average vehicle waiting times
- Lower fuel consumption and CO₂ emissions

## 🧩 Key Features

- **ACO algorithm implementation** with pheromone update and convergence logic
- **Simulation using SUMO + PLEXE** for cooperative vehicle behavior
- **Mathematical model** of traffic signals and convergence proofs
- **Parameter tuning** for α, ρ, C (pheromone weight, evaporation, cost penalty)
- **Visualizations** using `matplotlib` for performance metrics (fuel, emissions, wait time)

## 🛠️ Technologies Used

- `Python` — algorithmic implementation and simulation logic  
- `TensorFlow` — for optional ML-driven parameter tuning (in development)  
- `pandas`, `matplotlib` — data analysis and visualization  
- `SUMO`, `PLEXE` — for microscopic traffic simulation  
- `OMNeT++` — modeling communication in cooperative driving  
- `MATLAB` — complementary simulations for mathematical model validation

## 📊 Results

- Significant improvement in traffic flow vs. static light control
- Reduced fuel consumption and CO₂ emissions in simulation
- Verified convergence of ACO model under varied parameters

## 📂 Structure

