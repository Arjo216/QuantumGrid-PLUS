use pqcrypto_dilithium::dilithium3;
use pqcrypto_traits::sign::{PublicKey as _, SignedMessage as _}; 
use sha2::{Sha256, Digest};

// Proto & gRPC
pub mod sentinel {
    tonic::include_proto!("sentinel");
}
use sentinel::ai_sentinel_client::AiSentinelClient;
use sentinel::TransactionRequest;

// A struct to deserialize our Python API response
#[derive(serde::Deserialize)]
struct QuantumResponse {
    source: String,
    entropy_hex: String,
}

// Function to fetch and mix Quantum Entropy
async fn get_hybrid_entropy() -> Result<String, Box<dyn std::error::Error>> {
    println!("📡 Fetching True Entropy from Quantum Oracle...");
    
    let res = reqwest::get("http://127.0.0.1:5000/entropy")
        .await?
        .json::<QuantumResponse>()
        .await?;

    println!("   -> Source: {}", res.source);
    
    // Hash it via SHA256 to create a mathematically safe "Super Seed"
    let mut hasher = Sha256::new();
    hasher.update(res.entropy_hex.as_bytes());
    let mixed_seed = hex::encode(hasher.finalize());

    Ok(mixed_seed)
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("--- QUANTUMGRID PLUS: FULL SYSTEM BOOT ---");

    // 1. Fetch Quantum Entropy
    let quantum_seed = get_hybrid_entropy().await?;
    println!("✅ Hybrid Quantum-Classical Seed Pool Established.");
    println!("   -> Seed: {}...\n", &quantum_seed[0..24]);

    // 2. Generate Post-Quantum Keys
    println!("🔐 Generating NIST FIPS 204 (Dilithium3) Keys (Seeded)...");
    let (pk, sk) = dilithium3::keypair(); 
    let pk_hex = hex::encode(pk.as_bytes());
    
    println!("   -> Public Key Size: {} bytes", pk.as_bytes().len());
    println!("   -> Address: {}...{}", &pk_hex[0..20], &pk_hex[pk_hex.len()-20..]);

    // 3. Connect to the AI Sentinel
    println!("\n🔌 Connecting to AI Sentinel (gRPC)...");
    let mut client = AiSentinelClient::connect("http://127.0.0.1:50051").await?;

    // 4. Simulate a Transaction
    let amount = 1500.0;
    let signature = dilithium3::sign(b"Transfer 1500", &sk);
    
    let request = tonic::Request::new(TransactionRequest {
        tx_hash: "0xabc123789...".to_string(),
        sender_pqc_key: pk_hex,
        amount: amount,
        timestamp: 123456789,
        signature: signature.as_bytes().to_vec(),
    });

    // 5. Send the request and wait for the verdict
    let response = client.analyze_transaction(request).await?;
    let verdict = response.into_inner();

    println!("\n🤖 AI SENTINEL VERDICT:");
    if verdict.is_safe {
        println!("   ✅ APPROVED. Reason: {}", verdict.reason);
    } else {
        println!("   ⛔ BLOCKED. Reason: {}", verdict.reason);
        println!("   ⚠️  Risk Score: {}", verdict.risk_score);
    }

    Ok(())
}