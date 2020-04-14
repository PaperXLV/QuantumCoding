import cirq


def teleportation_circuit():
    # Setup three qubits
    qreg = [cirq.LineQubit(x) for x in range(3)]
    circ = cirq.Circuit()

    # Set 0 qubit to +
    circ.append([cirq.H(qreg[0])])

    # Prepare Bell pair with 1 and 2 qubit
    circ.append([cirq.H(qreg[1]),
                 cirq.CNOT(qreg[1], qreg[2])])

    # 3rd qubit would be sent to Bob at this point.

    # Teleportation protocol: apply CNOT and H, measure 0 and 1
    circ.append([cirq.CNOT(qreg[0], qreg[1]),
                 cirq.H(qreg[0]), cirq.measure(qreg[0], key='m0'),
                 cirq.measure(qreg[1], key="m1")])

    # Teleportation protocol: cnot and cz to restore state
    circ.append([cirq.CNOT(qreg[1], qreg[2]), cirq.CZ(qreg[0], qreg[2])])

    # Restore 0 from expected + state on qubit 2
    circ.append([cirq.H(qreg[2]), cirq.measure(qreg[2], key="final")])
    print("Circuit: ")
    print(circ)
    return circ


simulator = cirq.Simulator()
result = simulator.run(teleportation_circuit(), repetitions=10)
# All final measurements should be zero, as we teleported a + state, then applied H.
print(result)
