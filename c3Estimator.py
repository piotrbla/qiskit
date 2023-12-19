from qiskit_ibm_runtime import QiskitRuntimeService, Estimator, Options
from qiskit.quantum_info import Pauli
from qiskit import QuantumCircuit


service = QiskitRuntimeService(channel="ibm_quantum")

# Create a new circuit with two qubits (first argument) and two classical
# bits (second argument)
qc = QuantumCircuit(2)
qc.h(0) # Add a Hadamard gate to qubit 0
qc.cx(0, 1) # Perform a controlled-X gate on qubit 1, controlled by qubit 0

ZZ = Pauli('ZZ')
ZI = Pauli('ZI')
IZ = Pauli('IZ')
XX = Pauli('XX')
XI = Pauli('XI')
IX = Pauli('IX')
 
# service = QiskitRuntimeService()
 
# Run on the least-busy backend you have access to
backend = service.least_busy(simulator=True, operational=True)
 
options = Options()
options.resilience_level = 1
options.optimization_level = 3
 
# Create an Estimator object
estimator = Estimator(backend, options=options)
 
# Submit the circuit to Estimator
job = estimator.run(circuits=[qc]*6, observables=[IZ, IX, ZI, XI, ZZ, XX], shots = 5000)
 
# Once the job is complete, get the result
x_result = job.result()

print(type(x_result))
print(x_result)
