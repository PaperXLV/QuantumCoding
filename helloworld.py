import cirq

# Pick a qubit
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit.from_ops([
    cirq.X(qubit),  # NOT
    cirq.measure(qubit, key='m')  # Measure
])

print("Circuit:")
print(circuit)

simulator = cirq.Simulator()

result = simulator.run(circuit, repetitions=10)

print("Results")
print(result)
