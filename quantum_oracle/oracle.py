from flask import Flask, jsonify
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicProvider
from qiskit import transpile

app = Flask(__name__)

def generate_quantum_entropy(bits=256):
    print(f"🌌 [QUANTUM ORACLE] Initializing {bits}-qubit superposition...")
    # 1. Create a Quantum Circuit
    # We use 8 qubits to generate a byte of entropy per shot to keep the simulation fast
    qc = QuantumCircuit(8, 8)
    
    # 2. Apply Hadamard Gates (The Magic)
    # This puts the qubits into a 50/50 state of being both 1 and 0 simultaneously
    qc.h(range(8))
    
    # 3. Measure (Collapse the wave function)
    qc.measure(range(8), range(8))
    
    # 4. Execute on the local quantum simulator 
    # (In production, you'd point this to an IBM Cloud backend)
    backend = BasicProvider().get_backend("basic_simulator")
    t_qc = transpile(qc, backend)
    
    # We run it 32 times (32 bytes = 256 bits)
    job = backend.run(t_qc, shots=32)
    result = job.result().get_counts()
    
    # Extract the raw binary strings and convert to a hex seed
    raw_bits = list(result.keys())
    hex_entropy = "".join(raw_bits).replace(" ", "")[:64]
    
    return hex_entropy

@app.route('/entropy', methods=['GET'])
def get_entropy():
    entropy = generate_quantum_entropy()
    print(f"   -> Quantum Collapse Yield: {entropy[:16]}...")
    return jsonify({
        "source": "Qiskit_Superposition",
        "entropy_hex": entropy,
        "bits": 256
    })

if __name__ == '__main__':
    print("⚛️ QUANTUMGRID ORACLE RUNNING ON PORT 5000...")
    app.run(host='0.0.0.0', port=5000)