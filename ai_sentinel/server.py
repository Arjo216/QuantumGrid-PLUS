import grpc
from concurrent import futures
import sentinel_pb2
import sentinel_pb2_grpc
import torch
import torch.nn as nn

# We must define the same architecture to load the saved brain
class MEVAutoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(3, 2), nn.ReLU(), nn.Linear(2, 1))
        self.decoder = nn.Sequential(nn.Linear(1, 2), nn.ReLU(), nn.Linear(2, 3))
    def forward(self, x):
        return self.decoder(self.encoder(x))

class SentinelService(sentinel_pb2_grpc.AiSentinelServicer):
    def __init__(self):
        print("🧠 Loading PyTorch Autoencoder Weights...")
        self.model = MEVAutoencoder()
        # Load the trained model in evaluation mode
        self.model.load_state_dict(torch.load("mev_autoencoder.pth", weights_only=True))
        self.model.eval() 
        self.criterion = nn.MSELoss()
        print("🛡️ AI Sentinel Armed and Ready.")

    def AnalyzeTransaction(self, request, context):
        print(f"\n🔍 [AI BRAIN] Analyzing TX from: {request.sender_pqc_key[:15]}...")
        
        # 1. Normalize incoming gRPC data to match training scale
        amount_norm = request.amount / 1000.0
        time_norm = 0.5 # Simulated default time delta
        rep_norm = 1.0  # Simulated default sender reputation
        
        features = torch.FloatTensor([[amount_norm, time_norm, rep_norm]])
        
        # 2. AI Inference: Calculate Reconstruction Loss
        with torch.no_grad():
            reconstruction = self.model(features)
            loss = self.criterion(reconstruction, features).item()
        
        # 3. The Mathematics of Anomaly Detection
        # If the loss exceeds our strict threshold, the transaction is structurally abnormal
        ANOMALY_THRESHOLD = 0.05
        
        print(f"   -> Neural Reconstruction Loss: {loss:.4f} (Threshold: {ANOMALY_THRESHOLD})")
        
        if loss > ANOMALY_THRESHOLD:
            # Scale the mathematical loss to a 0.0-1.0 risk percentage
            risk_score = min(loss * 5.0, 1.0) 
            reason = "ANOMALY: STRUCTURAL_DEVIATION_DETECTED (Possible MEV/Zero-Day)"
            is_safe = False
        else:
            risk_score = loss
            reason = "SAFE: FITS_HISTORICAL_DISTRIBUTION"
            is_safe = True

        print(f"   -> Verdict: {'✅ PASS' if is_safe else '⛔ BLOCK'} (Risk: {risk_score:.2f})")
        
        return sentinel_pb2.RiskAssessment(is_safe=is_safe, risk_score=risk_score, reason=reason)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sentinel_pb2_grpc.add_AiSentinelServicer_to_server(SentinelService(), server)
    server.add_insecure_port('[::]:50051')
    print("🚀 QUANTUMGRID PLUS: AI SENTINEL RUNNING ON PORT 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()