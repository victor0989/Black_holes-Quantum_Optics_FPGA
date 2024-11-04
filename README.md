# Black_holes-Quantum_Optics_FPGA
Quantum Optical Structures and Black Hole Tensors in FPGA Circuits: A Comprehensive Guides 

Exploring quantum circuits by combining Non-Hermitian photonic band winding, skin effects, dark matter properties, and Hamiltonian synthesis equations.
![Quantum circuit signals and channels analysis](https://github.com/victor0989/Black_holes-Quantum_Optics_FPGA/blob/main/FPGA_I2C_PROTOCOL/Quantum%20Circuit.png?raw=true)

# Small steps -short -guide
Guide for Filtering Frequencies of Space Signals
Initial Preparations

1. Install Necessary Software:
2. Python: Make sure you have Python installed (preferably version 3.7 or higher).
3. Python Libraries:
[pip install numpy scipy matplotlib qiskit]

# VHDL and Tools: Ensure you have a VHDL development environment, such as ModelSim or Xilinx ISE, to simulate and test your VHDL circuits.
Set Up Your Environment:
If you plan to use Docker or Kubernetes, install and configure Docker on your system. Consider using Docker Compose to facilitate the management of multiple containers.
Modeling and Filtering Signals in Python

# QUANTUM MODELS
![States, quantum_dimensions](https://github.com/victor0989/Black_holes-Quantum_Optics_FPGA/blob/main/GNSS/Quantum_model.png?raw=true)

# Acquire and Preprocess the Signals:
Simulate or use data from signals coming from the telescope.
You can simulate data using NumPy.

# Practical: Qiskit, VHDL
simulate the signals from your I2C-inspired Python script using quantum channels and gates in Qiskit, we’ll convert the concept of digital signal states into quantum states. We’ll use qubits to represent SDA and SCL channels, encoding "high" and "low" states as quantum states 
∣0⟩∣0⟩ and ∣1⟩ ∣1⟩. 

![Circuit](https://github.com/victor0989/Black_holes-Quantum_Optics_FPGA/blob/main/Quantum_decoder_signals_GNSS.png?raw=true)


The start and stop conditions, as well as the clock pulses, will correspond to specific operations on these qubits, simulating transitions through quantum gates.

# Concept Overview
Qubits as Channels: We can assign two qubits to represent SDA and SCL.
Quantum Gates: We’ll use X, H, and CX (CNOT) gates to simulate changes, such as "start," "stop," and "bit transmission."
Quantum Circuit: The sequence will follow the original logic in your I2C script.

![Quantum_optics_signals_dark_matter](https://github.com/victor0989/Black_holes-Quantum_Optics_FPGA/blob/main/FPGA_I2C_PROTOCOL/Captura%20de%20pantalla%202024-09-22%20235917.png?raw=true)


# Other Quantum projects include these technologies
1. Intel 9 processors features, parallelization, vectorization techniques
2. Zephyr RTOS to investigate Realtime systems
3. VHDL for creating signals
4. Communication in Qiskit circuits

# Explanation of the Qiskit Code

Start Condition: Sets SDA to low (|0⟩) while keeping SCL high (|1⟩), simulating the beginning of communication.
Clock Pulse: Each clock_pulse function call toggles SCL to simulate a pulse.

Send Bit: Adjusts SDA according to the bit value (0 or 1) and follows it with a clock pulse.
Stop Condition: Sets SDA high while SCL is high, signaling the end of communication.
Output and Simulation

# RS232 Serial Communication in VHDL
RS232 communication is useful for transmitting data, such as the results of your FIR filter, from the FPGA to a computer or other device. Here is an example of an RS232 transmitter.

The resulting histogram will give you the probability distribution of final states, representing the state of the SDA and SCL channels after running through the transmission steps. This helps analyze the effects of each state transition in a quantum format. You can adapt this model to visualize or measure intermediate states, representing different parts of the communication sequence.

# Code
Code Description:
Inputs and Outputs:

# clk: Clock signal that controls the operation of the transmitter.
reset: Reset signal to restart the state of the transmitter.
tx_data: 8-bit data to be sent through the RS232 line.
start_tx: Signal that initiates the data transmission.
tx: Transmission line to send the data serially.
busy: Indicator that shows whether the transmitter is busy.
Constants:

# Frequency
CLK_FREQ: Clock frequency (adjustable according to your design).
BAUD_RATE: Baud rate for communication.
Finite State Machine (FSM):

# States
Different states (IDLE, START, DATA, STOP) are used to control the sequence of transmission.
Transmission Process:

# TX_signals
Upon receiving start_tx, the system begins to send the data in serial format.
The transmission of the start bit, data bits, and stop bit is managed.
How to Use It create a new project in Vivado and add this code in a new VHDL file.

# OPTICS_MODEL_IMAGE
![Detection_of_DIMENSIONS_OPTICS_SIGNALS](https://github.com/victor0989/Black_holes-Quantum_Optics_FPGA/blob/main/RS232_peripherals_analysis_signals/OPTICS_SIGNALS_DETECTION.png?raw=true)


# Compile design parameters
Compile the design and ensure there are no errors.
Configure the Artix-7 device and assign the input/output signals to the appropriate pins in the design.
Simulate the design to verify the data transmission.

This approach isn’t a direct analog to classical signals but provides insight into how quantum channels and logic gates can represent the same transitions in a quantum framework.
