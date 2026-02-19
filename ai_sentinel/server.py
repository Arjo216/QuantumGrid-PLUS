import grpc
from concurrent import futures
import sentinel_pb2
import sentinel_pb2_grpc

class SentinelService(sentinel_pb2_grpc.AiSentinelServicer):
    def AnalyzeTransaction(self, request, context):
        print(f"\n🔍 [AI BRAIN] Received TX: {request.tx_hash[:8]}...")
        print(f"   -> Amount: {request.amount} | Sender: {request.sender_pqc_key[:20]}...")

        # --- AI LOGIC (Simulated MEV Detection) ---
        # Rule: Extremely high value transfers are flagged for MEV front-running risk
        risk_score = 0.1
        reason = "SAFE_TRANSACTION"
        
        if request.amount > 1000.0:
            print("   ⚠️  ANOMALY: High Value Transaction Detected!")
            risk_score = 0.85
            reason = "POTENTIAL_MEV_SANDWICH_ATTACK"
        
        is_safe = risk_score < 0.7

        print(f"   -> Verdict: {'✅ PASS' if is_safe else '⛔ BLOCK'} (Score: {risk_score})")
        
        return sentinel_pb2.RiskAssessment(
            is_safe=is_safe,
            risk_score=risk_score,
            reason=reason
        )

def serve():
    # Start the gRPC server with 10 worker threads
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sentinel_pb2_grpc.add_AiSentinelServicer_to_server(SentinelService(), server)
    server.add_insecure_port('[::]:50051')
    print("🚀 QUANTUMGRID PLUS: AI SENTINEL RUNNING ON PORT 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()