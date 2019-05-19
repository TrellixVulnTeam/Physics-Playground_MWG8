from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import BasicAer
from qiskit import execute
from qiskit.tools.visualization import plot_histogram, plot_state_city

from qiskit import IBMQ
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor

q = QuantumRegister(4, 'q')
tmp = QuantumRegister(1, 'tmp')
res = ClassicalRegister(4, 'res')

print(oracle.qasm())

# %matplotlib inline
qc.draw(output='mpl')

backend = BasicAer.get_backend('qasm_simulator')

job = execute(qc, backend)
result = job.result()

counts = result.get_counts(qc)

print(counts)
plot_histogram(counts)

# Run on a IBMQ calculator
IBMQ.load_accounts()

print("Available backends:")
IBMQ.backends()

large_enough_devices = IBMQ.backends(filters=lambda x: x.configuration().n_qubits > 3 and not x.configuration().simulator)
backend = least_busy(large_enough_devices)

print("The best backend is " + backend.name())

job_exp = execute(qc, backend, shots=1024, max_credits=3)
job_monitor(job_exp)

result_exp = job_exp.result()

counts_exp = result_exp.get_counts(qc)
plot_histogram([counts_exp,counts])