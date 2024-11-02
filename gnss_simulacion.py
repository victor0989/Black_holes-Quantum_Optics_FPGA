# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, find_peaks
from qiskit import QuantumCircuit, Aer, execute

# Parámetros de la señal GNSS
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs)  # Tiempo de 0 a 1 segundo


# Crear una señal tipo chirp (frecuencia que cambia en el tiempo)
def generate_gnss_signal():
    signal = chirp(t, f0=100, f1=200, t1=1, method='linear')
    return signal


# Simulación de ruido
def add_noise(signal):
    noise = np.random.normal(0, 0.1, signal.shape)
    return signal + noise


# Función para encontrar picos en la señal
def detect_peaks(received_signal):
    peaks, _ = find_peaks(received_signal, height=0)
    return peaks


# Crear un circuito cuántico
def create_quantum_circuit(signal):
    qc = QuantumCircuit(1)  # Crear un circuito con 1 qubit

    # Aplicar una puerta X dependiendo del valor máximo de la señal
    if np.max(signal) > 0.5:
        qc.x(0)  # Aplicar la puerta X si la señal es fuerte

    qc.measure_all()  # Medir el qubit
    return qc


# Función principal
def main():
    # Generar señal GNSS
    gnss_signal = generate_gnss_signal()

    # Graficar la señal GNSS
    plt.figure(figsize=(10, 4))
    plt.plot(t, gnss_signal)
    plt.title('Señal GNSS (Chirp)')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.show()

    # Agregar ruido a la señal
    received_signal = add_noise(gnss_signal)

    # Graficar la señal recibida con ruido
    plt.figure(figsize=(10, 4))
    plt.plot(t, received_signal)
    plt.title('Señal GNSS Recibida con Ruido')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.show()

    # Detectar picos en la señal recibida
    peaks = detect_peaks(received_signal)

    # Graficar picos en la señal recibida
    plt.figure(figsize=(10, 4))
    plt.plot(t, received_signal)
    plt.plot(t[peaks], received_signal[peaks], "x")
    plt.title('Picos en la Señal GNSS Recibida')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.show()

    # Crear circuito cuántico basado en la señal
    qc = create_quantum_circuit(received_signal)

    # Simular el circuito cuántico
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend=simulator, shots=1024).result()
    counts = result.get_counts(qc)

    # Mostrar resultados del circuito cuántico
    print("Resultados del circuito cuántico:", counts)


# Ejecutar la función principal
if __name__ == "__main__":
    main()
