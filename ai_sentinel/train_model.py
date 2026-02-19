import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 1. Define the Neural Network Architecture
class MEVAutoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        # Input Features: [Amount, TimeDelta, SenderReputation]
        self.encoder = nn.Sequential(
            nn.Linear(3, 2),
            nn.ReLU(),
            nn.Linear(2, 1) # Compresses down to a 1D latent space
        )
        self.decoder = nn.Sequential(
            nn.Linear(1, 2),
            nn.ReLU(),
            nn.Linear(2, 3) # Attempts to reconstruct the 3 original features
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

# 2. Generate "Normal" Blockchain Traffic
def generate_training_data(samples=5000):
    print("📊 Generating 5,000 synthetic 'Safe' transactions...")
    # Normal amounts: 10 to 500, Normal Time Delta: 1 to 60s, Reputation: 0.8 to 1.0
    amounts = np.random.uniform(10, 500, samples) / 1000.0 # Normalized
    times = np.random.uniform(1, 60, samples) / 60.0       # Normalized
    reputations = np.random.uniform(0.8, 1.0, samples)     # Normalized
    
    data = np.column_stack((amounts, times, reputations))
    return torch.FloatTensor(data)

if __name__ == "__main__":
    train_data = generate_training_data()
    
    model = MEVAutoencoder()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    print("⚙️ Training Unsupervised Autoencoder...")
    for epoch in range(150):
        optimizer.zero_grad()
        outputs = model(train_data)
        loss = criterion(outputs, train_data)
        loss.backward()
        optimizer.step()
        
        if (epoch+1) % 30 == 0:
            print(f"   -> Epoch {epoch+1}/150 | Reconstruction Loss: {loss.item():.4f}")
            
    # Save the trained weights to disk
    torch.save(model.state_dict(), "mev_autoencoder.pth")
    print("✅ Production Model saved to 'mev_autoencoder.pth'")