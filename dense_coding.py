import cirq
import numpy as np


def dense_circuit():
    # Setup 2 qubits
    alice, bob = cirq.LineQubit.range(2)
    c = cirq.Circuit()

    # Setup Bell state
    c.append([cirq.H(alice),
              cirq.CNOT(alice, bob)])

    # 2nd qubit would be sent to bob at this point

    # Decide message
    message = np.random.choice([0, 1], size=2)
    # Modify alice's qubit
    if message[1]:
        c.append([cirq.X(alice)])
    if message[0]:
        c.append([cirq.Z(alice)])
    print("Message: ", message[0], message[1])
    # 1st qubit would be sent to bob at this point

    c.append([cirq.CNOT(alice, bob), cirq.H(alice),
              cirq.measure(alice, bob, key="m"), ])

    print("Circuit:")
    print(c)
    return c


simulator = cirq.Simulator()
result = simulator.run(dense_circuit(), repetitions=10)
# measurement outcomes should match message printout
print(result)
