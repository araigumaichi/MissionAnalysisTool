# Design Brief: Space Systems Mission Analysis Tool

## Objective
Develop a Python-based numerical simulation tool for space systems mission analysis. The tool will be designed using object-oriented programming (OOP) and test-driven development (TDD) principles. It will employ vectorized computations using the `numpy` and `dask` libraries to ensure high performance, avoiding explicit loops. Visualization capabilities will be included via `matplotlib`.

---

## Design Requirements

### General Design Principles
- **Object-Oriented Programming (OOP):** Utilize generic classes where possible, followed by specific subclasses for models and functionality.
- **Test-Driven Development (TDD):** Implement unit tests for all core functionalities.
- **Vectorized Computations:** Avoid `for` loops; instead, leverage `dask` for parallelized and distributed computations.
- **Logical Separation:** Organize functions and classes into thematic modules, such as `Time`, `Body`, `Trajectory`, `Perturbations`, etc.

---

## Core Functionalities

### Time Management
- Implement an `AbsoluteTime` class to handle simulation start and end times.

### Orbited Bodies
- Create a generic `Body` class with key attributes:
  - J2 (second zonal harmonic coefficient)
  - Flattening
  - Radii of ellipsoid (equatorial and polar radii)
  - Mass
  - Rotation rate
  - Other key characteristics such as gravitational parameter and reference atmospheric model (if applicable).
- Develop specific subclasses: `Earth`, `Moon`, `Mars`, incorporating relevant planetary parameters.

### Reference Frames
- Support Earth-Centered Inertial (ECI) and Earth-Centered Earth-Fixed (ECEF) frames.

### Trajectory Propagation
- Implement basic propagators:
  - **Keplerian Model:** Based on orbital elements.
  - **Position-Velocity (PV) Model:** Using initial state vectors.
- Allow for extensibility to add more complex propagation methods.

### Orbital Elements & Anomalies
- Compute all six Keplerian elements.
- Support anomaly conversion functions:
  - True Anomaly ↔ Mean Anomaly ↔ Eccentric Anomaly.

### Satellite Kinematics
- Compute:
  - Position, velocity, and acceleration in Cartesian coordinates.
  - Satellite-Sun direction vector.
  - Shadowing effects from orbited bodies.
  - Solar panel orientation based on Sun vector and panel normal.
  - Longitude-latitude-altitude conversion from Cartesian coordinates.

### Satellite Attitude
- Implement attitude representation using Euler angles (roll-pitch-yaw) in Local Orbital Frame (LOF).

### Thrust Modeling
- Implement continuous and instantaneous thrust models.

### Satellite Characteristics
- Define core properties: mass, cross-section surface, characteristic size.

### Atmospheric Model
- Implement a basic atmospheric density model as a function of altitude. 
### External Perturbations
- Create a generic `Perturbation` class and derive specific subclasses for:
  - **Aerodynamic Drag:** Based on simple atmospheric density model.
  - **Gravitational Field:** Implement basic Earth gravity variations.
  - **Solar Radiation Pressure:** Consider radiation forces on satellite.
  - **Gravity Gradient Torque:** Compute effects based on satellite orientation.

### Visualization & Plots
- **3D Trajectory Visualization:** Plot orbital trajectory around the orbited body.
- **2D Ground Track Map:** Display trajectory using longitude-latitude coordinates on a world map.

---

## Future Improvements (Not to be Implemented Now)
- Earth albedo and infrared radiation modeling.
- Internal perturbations such as fuel sloshing.
- Advanced aerodynamic modeling including wind effects.
- Telecommunications models (link budget, availability, traffic, inter-satellite links).

---

## Conclusion
This tool will provide a robust numerical simulation framework for space mission analysis, ensuring modularity, extensibility, and high computational efficiency. Future enhancements will further expand its capabilities for mission planning and analysis.