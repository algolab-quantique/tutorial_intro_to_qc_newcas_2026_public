from qiskit.circuit.random import random_circuit


def black_box():
    U = random_circuit(num_qubits=5, depth=10, seed=int(hash("algolab2025")) % 10**5)
    return U
