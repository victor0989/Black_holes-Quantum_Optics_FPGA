from qiskit import QuantumCircuit, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator

# Define the circuit
qc = QuantumCircuit(2, 2)

# Start condition
qc.x(0)  # SDA high
qc.x(1)  # SCL high
qc.barrier()
qc.x(0)  # SDA low for start

# Clock pulse
def clock_pulse(qc):
    qc.x(1)  # SCL low
    qc.barrier()
    qc.x(1)  # SCL high
    qc.barrier()

# Send bit function
def send_bit(qc, bit):
    if bit == 1:
        qc.x(0)  # SDA high if bit is 1
    else:
        qc.x(0)  # SDA low if bit is 0
    clock_pulse(qc)

# Transmit example sequence
send_bit(qc, 1)
send_bit(qc, 0)
send_bit(qc, 1)
send_bit(qc, 1)

# Stop condition
qc.x(0)  # SDA high for stop

# Measurement
qc.measure(0, 0)  # Measure SDA
qc.measure(1, 1)  # Measure SCL

# Use AerSimulator to execute the circuit
simulator = AerSimulator()
qc.save_statevector()  # Save the statevector for analysis
job = simulator.run(qc, shots=1024)
result = job.result()

# Get the measurement results
counts = result.get_counts(qc)

# Visualize the circuit and measurement results
print("Quantum Circuit:")
print(qc.draw(output='text'))
plot_histogram(counts)
plt.show()
