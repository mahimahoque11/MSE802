import os
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator

script_dir = os.path.dirname(__file__) 

file_path = os.path.join(script_dir, "myfile.qasm")

print(f"--- Attempting to load: {file_path} ---")

try:

    circuit = QuantumCircuit.from_qasm_file(file_path)

    backend = BasicSimulator()
    
    job = backend.run(circuit)
    result = job.result()

    counts = result.get_counts()
    print("\nSuccess! Quantum Measurement Results:")
    print(counts)
    
    print("\nVisual Circuit Diagram:")
    print(circuit.draw(output='text'))

except FileNotFoundError:
    print(f"\nERROR: Could not find 'myfile.qasm' in {script_dir}")
    print("Double-check that the filename in the sidebar matches exactly.")
except Exception as e:
    print(f"\nAn error occurred: {e}")