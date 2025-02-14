# Traveling Salesman Problem (TSP) - Simulated Annealing for Qatar

## Overview
This project implements a **Simulated Annealing** algorithm to solve the **Traveling Salesman Problem (TSP)** for a dataset of **Qatar cities**. The algorithm attempts to find an optimized route that minimizes the total travel distance.

## Features
- Uses **Simulated Annealing** for optimization.
- Reads **city coordinates** from a dataset.
- Computes **pairwise distances** between cities.
- Iteratively refines the solution using a probabilistic approach.
- Visualizes the final optimized route using **Matplotlib**.

## Algorithm - Simulated Annealing
The **Simulated Annealing** approach works by:
1. Starting with a **random tour** of cities.
2. Making **small modifications** to the tour by swapping segments.
3. Accepting a new tour based on:
   - If it's **better (shorter distance)**.
   - If it's **worse, with a probability** that depends on a decreasing **temperature parameter (T)**.
4. Gradually reducing **T** to limit randomness over time.
5. Stopping when **error tolerance is reached**.

### **Input File Format**
The program reads city coordinates from a text file (e.g., `data194.txt`). 

## Configuration Parameters
You can modify these parameters in the script:
- **Initial Temperature (T)**: `T=100`
- **Cooling Rate (r)**: `r=0.9`
- **Exact Optimal Distance** (for error calculation): `exact=9352`
