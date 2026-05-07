from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere, plot_bloch_multivector
import matplotlib.pyplot as plt

qc = QuantumCircuit(2)
qc.h([0, 1])
qc.s(0) 

state = Statevector.from_instruction(qc)

print("Generating plots...")
plot_state_qsphere(state)
# plot_bloch_multivector(state) # Uncomment this if you want to see both!

plt.show()