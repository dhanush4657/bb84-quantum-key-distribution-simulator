# core/qiskit_mode.py   (NEW FILE - OPTIONAL RESUME BOOST)

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# bit + basis -> real quantum circuit
def create_qubit(bit, basis):
    qc = QuantumCircuit(1, 1)

    # Prepare bit in Z basis
    if bit == 1:
        qc.x(0)

    # Convert to X basis if needed
    if basis == "X":
        qc.h(0)

    return qc


# Bob measures in chosen basis
def measure_qubit(bit, alice_basis, bob_basis):

    qc = create_qubit(bit, alice_basis)

    # If Bob measures in X basis
    if bob_basis == "X":
        qc.h(0)

    qc.measure(0, 0)

    sim = AerSimulator()
    result = sim.run(qc, shots=1).result()

    counts = result.get_counts()

    measured = int(list(counts.keys())[0])

    return measured