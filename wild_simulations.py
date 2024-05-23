import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("10 Wild Simulations")

# 1. Dark Matter Simulation
def dark_matter_simulation():
    x = np.random.normal(0, 1, 1000)
    y = np.random.normal(0, 1, 1000)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.5, s=1, color='black')
    plt.title('Dark Matter Distribution Simulation')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    st.pyplot(plt)

st.header("1. Dark Matter Simulation")
dark_matter_simulation()

# 2. Quantum Entanglement Visualization
def quantum_entanglement_visualization():
    theta = np.linspace(0, 2 * np.pi, 100)
    x1 = np.sin(theta)
    y1 = np.cos(theta)
    x2 = np.sin(theta + np.pi)
    y2 = np.cos(theta + np.pi)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x1, y1, label='Particle 1')
    plt.plot(x2, y2, label='Particle 2')
    plt.title('Quantum Entanglement Visualization')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    st.pyplot(plt)

st.header("2. Quantum Entanglement Visualization")
quantum_entanglement_visualization()

# 3. Quantum Tunneling Simulation
def quantum_tunneling_simulation():
    x = np.linspace(-2, 2, 500)
    potential = np.piecewise(x, [x < -1, (x >= -1) & (x <= 1), x > 1], [0, 1, 0])
    wavefunction = np.exp(-x**2) * np.cos(5 * x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, potential, label='Potential Barrier')
    plt.plot(x, wavefunction, label='Wavefunction')
    plt.title('Quantum Tunneling Simulation')
    plt.xlabel('X Position')
    plt.ylabel('Potential / Wavefunction')
    plt.legend()
    st.pyplot(plt)

st.header("3. Quantum Tunneling Simulation")
quantum_tunneling_simulation()

# 4. Gravitational Wave Detection
def gravitational_wave_detection():
    t = np.linspace(0, 10, 1000)
    wave1 = np.sin(2 * np.pi * t)
    wave2 = np.sin(2 * np.pi * t + np.pi / 2)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, wave1, label='Gravitational Wave 1')
    plt.plot(t, wave2, label='Gravitational Wave 2')
    plt.title('Gravitational Wave Detection')
    plt.xlabel('Time')
    plt.ylabel('Wave Amplitude')
    plt.legend()
    st.pyplot(plt)

st.header("4. Gravitational Wave Detection")
gravitational_wave_detection()

# 5. Superconductivity at Room Temperature
def superconductivity_visualization():
    temperatures = np.linspace(50, 300, 100)
    resistance = np.piecewise(temperatures, [temperatures < 200, temperatures >= 200], [lambda x: 100 - x, 0])
    
    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, resistance)
    plt.title('Superconductivity at Room Temperature')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Resistance (Ohms)')
    st.pyplot(plt)

st.header("5. Superconductivity at Room Temperature")
superconductivity_visualization()

# 6. Quantum Computing Performance
def quantum_computing_performance():
    qubits = np.arange(1, 21)
    performance = np.exp(qubits / 5)
    
    plt.figure(figsize=(10, 6))
    plt.plot(qubits, performance)
    plt.title('Quantum Computing Performance')
    plt.xlabel('Number of Qubits')
    plt.ylabel('Computational Power')
    st.pyplot(plt)

st.header("6. Quantum Computing Performance")
quantum_computing_performance()

# 7. AI Discovering New Particles
def particle_discovery_visualization():
    energy = np.linspace(0, 100, 1000)
    signal = np.exp(-0.1 * (energy - 50)**2)
    
    plt.figure(figsize=(10, 6))
    plt.plot(energy, signal)
    plt.title('AI Discovering New Particles')
    plt.xlabel('Energy (GeV)')
    plt.ylabel('Signal Strength')
    st.pyplot(plt)

st.header("7. AI Discovering New Particles")
particle_discovery_visualization()

# 8. Time Dilation Visualization
def time_dilation_visualization():
    velocity = np.linspace(0, 0.99, 100)
    time_dilation = 1 / np.sqrt(1 - velocity**2)
    
    plt.figure(figsize=(10, 6))
    plt.plot(velocity, time_dilation)
    plt.title('Time Dilation Visualization')
    plt.xlabel('Velocity (c)')
    plt.ylabel('Time Dilation Factor')
    st.pyplot(plt)

st.header("8. Time Dilation Visualization")
time_dilation_visualization()

# 9. Multi-Dimensional Space Simulation
def multi_dimensional_space_simulation():
    from mpl_toolkits.mplot3d import Axes3D
    
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    x = np.random.normal(0, 1, 100)
    y = np.random.normal(0, 1, 100)
    z = np.random.normal(0, 1, 100)
    
    ax.scatter(x, y, z)
    ax.set_title('Multi-Dimensional Space Simulation')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    st.pyplot(fig)

st.header("9. Multi-Dimensional Space Simulation")
multi_dimensional_space_simulation()

# 10. Quantum Field Theory Visualization
def quantum_field_theory_visualization():
    x = np.linspace(-10, 10, 1000)
    field = np.sin(2 * np.pi * x) * np.exp(-x**2 / 10)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, field)
    plt.title('Quantum Field Theory Visualization')
    plt.xlabel('Position')
    plt.ylabel('Field Strength')
    st.pyplot(plt)

st.header("10. Quantum Field Theory Visualization")
quantum_field_theory_visualization()
