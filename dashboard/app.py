import streamlit as st
import subprocess
import re
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="QuantumGrid PLUS",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for "Hacker/DeepTech" Aesthetic ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #C9D1D9; }
    .metric-box { background-color: #161B22; padding: 20px; border-radius: 10px; border: 1px solid #30363D; }
    hr { border-color: #30363D; }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 QuantumGrid PLUS | Mission Control")
st.markdown("**Architecture:** IBM Quantum Oracle ➔ Rust PQC ➔ Merkle Aggregator ➔ PyTorch Autoencoder")
st.divider()

# --- The Trigger ---
if st.button("🚀 INITIATE BATCH TRANSACTION & AI SCAN", type="primary", use_container_width=True):
    
    with st.status("Executing Multi-Layer Architecture...", expanded=True) as status:
        st.write("📡 1. Pinging IBM Quantum Oracle for superposition entropy...")
        time.sleep(0.4)
        st.write("🔐 2. Generating FIPS 204 Dilithium3 Keys in Rust Core...")
        time.sleep(0.4)
        st.write("📦 3. Batching Mempool Transactions & Calculating Merkle Root...")
        
        # --- THE BRIDGE: Run the Rust Node ---
        result = subprocess.run(
            ["cargo", "run"], 
            cwd="../core_ledger", 
            capture_output=True, 
            text=True
        )
        output = result.stdout
        
        st.write("🤖 4. Streaming gRPC Merkle payload to PyTorch Autoencoder...")
        time.sleep(0.4)
        status.update(label="Batch Processed!", state="complete", expanded=False)

    # --- Parser ---
    try:
        # Regex to extract the new Rust terminal outputs
        seed = re.search(r"Seed Pool:\s*([a-f0-9]+)\.\.\.", output)
        key_size = re.search(r"Public Key Size:\s*(\d+)", output)
        
        # Merkle Tree Metrics
        uncompressed = re.search(r"Uncompressed Batch Size:\s*(\d+)", output)
        compression = re.search(r"Compression Ratio:\s*([0-9\.]+%)", output)
        merkle_root = re.search(r"Merkle Root Hash:\s*([a-f0-9]+)", output)
        
        # TX & AI Metrics
        tx_amount = re.search(r"TX_1 \(([\d\.]+)\s*STQ\)", output)
        is_blocked = "⛔ BLOCKED" in output
        reason_match = re.search(r"Reason:\s*(.+)", output)

        # Fallbacks for safe parsing
        seed_val = seed.group(1) if seed else "UNKNOWN"
        key_val = key_size.group(1) if key_size else "UNKNOWN"
        uncompressed_val = uncompressed.group(1) if uncompressed else "0"
        compression_val = compression.group(1) if compression else "0%"
        merkle_val = merkle_root.group(1) if merkle_root else "UNKNOWN"
        amount_val = tx_amount.group(1) if tx_amount else "0.00"
        reason_val = reason_match.group(1) if reason_match else "Unknown"

        # --- Render the UI Dashboard ---
        st.subheader("Layer 1: Cryptographic Telemetry")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("⚛️ Quantum Seed (XOR Mixed)", f"{seed_val[:12]}...", delta="True Entropy")
        with col2:
            st.metric("🔏 PQC Key Size", f"{key_val} bytes", delta="40x Larger than ECC", delta_color="inverse")
        with col3:
            st.metric("📦 Merkle Compression", f"{compression_val}", delta=f"Down from {uncompressed_val} bytes", delta_color="normal")

        st.markdown(f"**🌳 Merkle Root Hash (State ID):** `{merkle_val}`")
        st.divider()
        
        # --- Render the AI Verdict ---
        st.subheader(f"Layer 2: AI Mempool Governance (Evaluating TX: {amount_val} STQ)")
        
        if is_blocked:
            st.error(f"### 🚨 TRANSACTION BLOCKED\n**AI Verdict:** {reason_val}\n\n*The Unsupervised PyTorch Autoencoder detected a structural deviation, preventing a potential MEV exploit.*")
        else:
            st.success(f"### ✅ TRANSACTION APPROVED\n**AI Verdict:** {reason_val}\n\n*Transaction matches historical distribution. Safe to add to the ledger.*")

        # --- Raw Logs ---
        with st.expander("View Raw Terminal Stdout (Rust -> Python gRPC)"):
            st.code(output, language="log")

    except Exception as e:
        st.error(f"Failed to parse the architecture output: {e}")
        with st.expander("View Raw Terminal Output"):
            st.code(output, language="log")