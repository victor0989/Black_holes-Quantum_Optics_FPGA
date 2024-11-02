from qiskit import QuantumCircuit, Aer, transpile
from qiskit_aer import AerSimulator  # Importar AerSimulator
from qiskit.visualization import plot_histogram

# Crear un circuito cuántico con 1 qubit y 1 bit clásico
circuit = QuantumCircuit(1, 1)

# Aplicar la puerta Hadamard para crear superposición
circuit.h(0)

# Supongamos que queremos filtrar ciertas frecuencias
# Aquí puedes implementar un mecanismo de filtrado
# Ejemplo: Si la frecuencia está en un rango específico, aplicamos una puerta X (que invierte el qubit)

# Condiciones para el filtrado (ejemplo simplificado)
# Puedes definir condiciones reales o señales a filtrar
frequency_condition = True  # Cambiar a False para simular un caso donde se rechaza la señal

if frequency_condition:
    circuit.x(0)  # Aplicar puerta X si la condición es verdadera

# Medir el qubit y almacenar el resultado en el bit clásico
circuit.measure(0, 0)

# Mostrar el circuito
print(circuit)

# Usar AerSimulator
simulator = AerSimulator()  # Crear una instancia de AerSimulator

# Ejecutar el circuito
job = simulator.run(circuit, shots=1024)  # Ejecutar el circuito con el simulator
result = job.result()

# Obtener y mostrar los resultados
counts = result.get_counts(circuit)
print("Resultados de la medición:", counts)

# Opcional: Mostrar un histograma de los resultados
#plot_histogram(counts).show()
