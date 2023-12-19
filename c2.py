from qiskit.quantum_info import Pauli
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
ZZ = Pauli('ZZ')
ZI = Pauli('ZI')
IZ = Pauli('IZ')
XX = Pauli('XX')
XI = Pauli('XI')
IX = Pauli('IX')
qc.append(ZZ, [0, 1])
qc.append(ZI, [0, 1])

qc.draw(output='latex', filename='quantum_circuit3.png')


 