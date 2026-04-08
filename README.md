<div align="center">

# 🌌 QuantumGrid PLUS
**The AI-Governed, Quantum-Sovereign Immutable Ledger**

[![Rust](https://img.shields.io/badge/Rust-1.70+-orange.svg)](https://www.rust-lang.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c.svg)](https://pytorch.org/)
[![Cryptography](https://img.shields.io/badge/NIST-FIPS%20204%20(Dilithium3)-blue.svg)](https://csrc.nist.gov/)
[![Quantum](https://img.shields.io/badge/IBM-Qiskit%20Superposition-purple.svg)](https://quantum.ibm.com/)
[![Architecture](https://img.shields.io/badge/Microservices-gRPC%20%7C%20Protobuf-244c5a.svg)](https://grpc.io/)

QuantumGrid PLUS is a flagship DeepTech infrastructure prototype designed to address the "Four Horsemen" of next-generation computer science: **Post-Quantum Cryptography (PQC), Quantum Computing, Blockchain, and Machine Learning.**

It acts as a next-generation Layer-1 node architecture that replaces legacy elliptic curve cryptography with quantum-resistant identities, eliminates PQC data bloat via Merkle Tree aggregation, and utilizes an unsupervised Deep Learning Autoencoder to detect zero-day MEV (Maximal Extractable Value) exploits in the mempool before consensus.

</div>

---

## 🚀 The Architecture (4-Tier Microservices)

Unlike monolithic blockchains, QuantumGrid PLUS operates on a highly decoupled, fault-tolerant gRPC architecture.

### 1. The Quantum Oracle (`Python/Flask + IBM Qiskit`)
Standard CSPRNGs (Pseudo-Random Number Generators) rely on deterministic OS noise, creating vulnerabilities for wallet generation. The Oracle forces qubits into a 50/50 superposition state, measures the physical collapse of the wave function, and returns true physical entropy. To prevent API single-point-of-failure, this is **XOR-hashed with local OS entropy** to create a secure Hybrid Seed.

### 2. The Core Ledger (`Rust + FIPS 204`)
Written in high-performance memory-safe Rust, the core handles Post-Quantum identity generation. It implements **NIST FIPS 204 (Dilithium3)** standards. 
**The Bloat Solution:** Because Dilithium3 signatures are massive (~3,300 bytes), the Rust core batches transactions and calculates a **Merkle Tree Root**. This cryptographic aggregation compresses batch state verification down to a single 32-byte hash, achieving a **99.8% space savings** on-chain.

### 3. The AI Sentinel (`Python + PyTorch + gRPC`)
Instead of hardcoded consensus rules, the mempool is governed by an Unsupervised PyTorch Autoencoder. The Neural Network was trained on thousands of "normal" blockchain states. When a new gRPC transaction payload arrives, the network attempts to reconstruct the data.
* **Mathematical Anomaly Detection:** $MSE = \frac{1}{n}\sum_{i=1}^{n}(Y_i - \hat{Y_i})^2$. If the Mean Squared Error (Reconstruction Loss) exceeds strict structural thresholds (e.g., a predatory MEV front-running pattern), the transaction is blocked before propagating to peer nodes.

### 4. Mission Control (`Streamlit UI`)
A real-time, interactive frontend that visually breaks down the gRPC telemetry, Merkle compression ratios, and live AI neural reconstruction loss scoring.

---

## 🛠️ System Flow Diagram

```mermaid
flowchart TD
    %% ==========================================
    %% CUSTOM CSS & DEEPTECH COLOR PALETTE
    %% ==========================================
    classDef webUI fill:#0E1117,stroke:#58A6FF,stroke-width:2px,color:#C9D1D9,rx:10px,ry:10px
    classDef rustCore fill:#B7410E,stroke:#FFA500,stroke-width:2px,color:#FFFFFF,rx:5px,ry:5px
    classDef quantumAPI fill:#6929C4,stroke:#A56EFF,stroke-width:2px,color:#FFFFFF,rx:8px,ry:8px
    classDef pythonAI fill:#306998,stroke:#FFD43B,stroke-width:2px,color:#FFFFFF,rx:5px,ry:5px
    classDef torchModel fill:#EE4C2C,stroke:#FF9885,stroke-width:2px,color:#FFFFFF,rx:5px,ry:5px
    classDef decisionPass fill:#238636,stroke:#3FB950,stroke-width:3px,color:#FFFFFF
    classDef decisionBlock fill:#DA3633,stroke:#FF7B72,stroke-width:3px,color:#FFFFFF
    classDef logicNode fill:#1F2328,stroke:#8B949E,stroke-width:2px,color:#E6EDF3,rx:20px,ry:20px

    %% ==========================================
    %% ARCHITECTURAL SUBGRAPHS
    %% ==========================================
    
    subgraph Frontend ["🖥️ MISSION CONTROL (Port 8501)"]
        UI["Streamlit Interactive Telemetry<br/>Dashboard & RegEx Parser"]:::webUI
    end

    subgraph QPU_Layer ["🌌 QUANTUM ORACLE (Port 5000)"]
        Flask["Python/Flask API Server"]:::pythonAI
        IBM[("IBM Qiskit QPU<br/>(Superposition Collapse)")]:::quantumAPI
        Flask <-->|Measures Physical Qubits| IBM
    end

    subgraph Rust_Ledger ["⚙️ LAYER 1: RUST CORE (FIPS 204)"]
        RustInit["Tokio Async Runtime<br/>(Transaction Batcher)"]:::rustCore
        PQC["Dilithium3 Keygen<br/>(XOR-Hashed Seed)"]:::rustCore
        Merkle["Merkle Tree Aggregator<br/>(99.8% Data Compression)"]:::rustCore
        
        RustInit --> PQC
        PQC --> Merkle
    end

    subgraph PyTorch_Brain ["🧠 AI SENTINEL (Port 50051)"]
        GRPC["gRPC / Protobuf Receiver"]:::pythonAI
        Autoencoder["Unsupervised PyTorch Autoencoder<br/>(Normalized Inference)"]:::torchModel
        MSE{"Calculate MSE<br/>Reconstruction Loss"}:::logicNode
        
        GRPC --> Autoencoder
        Autoencoder --> MSE
    end

    %% ==========================================
    %% DATA FLOW & NETWORK ROUTING
    %% ==========================================

    UI -- "1. Initiate Execution" --> RustInit
    RustInit -- "2. HTTP GET /entropy" --> Flask
    Flask -. "3. Returns Raw Entropy" .-> PQC
    
    Merkle -- "4. High-Speed Protobuf Payload" --> GRPC
    
    MSE -- "Loss < 0.05" --> Pass["✅ APPROVED<br/>(Safe Distribution)"]:::decisionPass
    MSE -- "Loss > 0.05" --> Block["🚨 BLOCKED<br/>(MEV Anomaly)"]:::decisionBlock
    
    Pass -- "5. Return Verdict" --> UI
    Block -- "5. Return Verdict" --> UI
```

### ⚙️ Quick Start Guide (GitHub Codespaces)
This project is fully dockerized and optimized for a cloud-native DevContainer environment.

1. Boot the Quantum Oracle (Terminal 1)

```Bash
cd quantum_oracle
python3 oracle.py
```
# Runs on localhost:5000

2. Boot the Deep Learning Brain (Terminal 2)

```Bash
cd ai_sentinel
python3 server.py
```
# Runs on gRPC port 50051

3. Launch Mission Control (Terminal 3)

```Bash
cd dashboard
streamlit run app.py
```
# Opens interactive UI in browser (Port 8501)

(Note: The Rust Core is executed dynamically by the Streamlit UI to demonstrate live transaction batches, data compression, and real-time AI inference).


### 📊 Security & SWOT Highlights
* **NIST-Aligned Sovereignty:** Utilizes FIPS 204 (Dilithium3) standards, effectively mitigating "Harvest Now, Decrypt Later" attacks by Shor's Algorithm.

* **Hybrid Entropy Resiliency:** Does not rely solely on the Quantum QPU. It XOR-hashes Quantum bits with Classical OS bits, preventing single-point-of-failure API dependency.

* **Fault-Tolerant AI Governance:** The AI runs out-of-band via gRPC. If the AI service crashes, the Rust blockchain core remains online and defaults to strict security parameters.


### 📊 DeepTech Innovations & Metrics
* **PQC Data Optimization:** Successfully reduced 13,000+ byte transaction batches to a 32-byte verifiable state identifier (Merkle Root).

* **Deterministic ML Bypassed:** Shifted from static rules to dynamic statistical reconstruction, allowing the node to detect unknown (zero-day) economic attacks based purely on mathematical deviation.

* **High-Speed IPC:** Replaced standard REST JSON APIs with Google's Protocol Buffers (Protobuf) over HTTP/2, ensuring the AI inference step does not bottleneck the blockchain's TPS (Transactions Per Second).

* **Engineered for maximum security and autonomy.**

### 📜 License
Distributed under the **MIT License**. See LICENSE for more information.

<div align="center">


<b>Architected and Engineered for the Post-Quantum Era.</b>
</div>
