from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate, MCXGate, CXGate  # Añadir CXGate para CNOT
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt  # Importar matplotlib

# Definir las puertas
mcx_gate = MCXGate(3)  # Un gate de control múltiple con 3 controles
hadamard_gate = HGate()  # Puerta Hadamard
cnot_gate = CXGate()  # Puerta CNOT

# Crear un circuito cuántico
qc = QuantumCircuit(4, 4)  # 4 qubits y 4 bits clásicos para la medición
qc.append(hadamard_gate, [0])  # Aplicar Hadamard al qubit 0
qc.append(mcx_gate, [0, 1, 2, 3])  # Aplicar el gate MCX con 3 controles
qc.append(cnot_gate, [0, 1])  # Aplicar CNOT con qubit 0 como control y qubit 1 como objetivo

# Medir todos los qubits
qc.measure([0, 1, 2, 3], [0, 1, 2, 3])  # Medir los qubits y almacenar en bits clásicos

# Dibujar el circuito
qc.draw('mpl')  # Dibujar el circuito utilizando matplotlib
plt.title("Circuito Cuántico con Puertas Lógicas")  # Título del circuito

# Simular el circuito
simulator = AerSimulator()  # Crear una instancia de AerSimulator
job = simulator.run(qc, shots=1024)  # Ejecutar el circuito
result = job.result()  # Obtener resultados

# Obtener y mostrar los resultados
counts = result.get_counts(qc)  # Asegurarte de que estás usando el objeto correcto
print("Resultados de la medición:", counts)

# Mostrar un histograma de los resultados
plot_histogram(counts)

# Mostrar el gráfico y esperar un tiempo
plt.show(block=True)  # Mostrar el histograma y no cerrar inmediatamente

