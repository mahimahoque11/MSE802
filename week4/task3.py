
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicProvider 

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

backend = BasicProvider().get_backend('basic_simulator')
result = backend.run(qc).result()

print(result.get_counts())