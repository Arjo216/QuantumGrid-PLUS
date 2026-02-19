# 🌌 QuantumGrid PLUS
**The AI-Governed, Quantum-Sovereign Immutable Ledger**

QuantumGrid PLUS is a flagship DeepTech infrastructure prototype designed to address the "Four Horsemen" of next-generation computer science: **Post-Quantum Cryptography (PQC), Quantum Computing, Blockchain, and Machine Learning.**

It acts as a next-generation Layer-1 node architecture that generates quantum-resistant identities and uses an AI-driven Mempool Sentinel to detect predatory network behavior (like MEV Sandwich Attacks) in real-time.

## 🚀 The Architecture

This project is built as a 3-tier microservice architecture:

1. **The Quantum Oracle (Python/Flask + IBM Qiskit):** Generates true physical entropy by forcing qubits into superposition, measuring the collapse, and returning the raw cryptographic noise.
2. **The Core Ledger (Rust + NIST FIPS 204):** A high-speed systems backend that fetches the quantum entropy, hashes it with local OS entropy (Hybrid Seed), and generates massive `Dilithium3` Post-Quantum signatures.
3. **The AI Sentinel (Python + PyTorch + gRPC):** A decoupled Deep Learning brain that receives pending transactions via fast Protocol Buffers (gRPC) and flags economic anomalies before they hit the consensus layer.

## 🛠️ Tech Stack
* **Systems/Core:** Rust, Tokio (Async), `pqcrypto-dilithium`
* **Networking:** gRPC, Protocol Buffers (Protobuf)
* **AI/Machine Learning:** Python, PyTorch (TorchScript ready)
* **Quantum:** IBM Qiskit Framework
* **DevOps:** GitHub Codespaces (Dockerized DevContainer)

## ⚙️ How to Run the Prototype

This project is optimized for GitHub Codespaces. 

**1. Start the AI Sentinel (gRPC Port 50051)**
```bash
cd ai_sentinel
python3 server.py
2. Start the Quantum Oracle (HTTP Port 5000)

Bash
cd quantum_oracle
python3 oracle.py
3. Execute the Post-Quantum Handshake

Bash
cd core_ledger
cargo run
📊 Security & SWOT Highlights
NIST-Aligned Sovereignty: Utilizes FIPS 204 (Dilithium3) standards, effectively mitigating "Harvest Now, Decrypt Later" attacks by Shor's Algorithm.

Hybrid Entropy Resiliency: Does not rely solely on the Quantum QPU. It XOR-hashes Quantum bits with Classical OS bits, preventing single-point-of-failure API dependency.

Fault-Tolerant AI Governance: The AI runs out-of-band via gRPC. If the AI service crashes, the Rust blockchain core remains online and defaults to strict security parameters.