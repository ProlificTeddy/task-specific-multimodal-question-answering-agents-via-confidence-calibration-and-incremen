import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class ConfidenceCalibratedTossupAgent(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(ConfidenceCalibratedTossupAgent, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        logits = self.fc2(x)
        confidence = self.softmax(logits)
        return logits, confidence

    def decide_to_answer(self, confidence, threshold=0.7):
        max_confidence, _ = torch.max(confidence, dim=-1)
        return max_confidence > threshold

class MultimodalBonusAgent(nn.Module):
    def __init__(self, text_dim, image_dim, hidden_dim, output_dim):
        super(MultimodalBonusAgent, self).__init__()
        self.text_fc = nn.Linear(text_dim, hidden_dim)
        self.image_fc = nn.Linear(image_dim, hidden_dim)
        self.combined_fc = nn.Linear(hidden_dim * 2, output_dim)

    def forward(self, text_features, image_features):
        text_out = F.relu(self.text_fc(text_features))
        image_out = F.relu(self.image_fc(image_features))
        combined_features = torch.cat((text_out, image_out), dim=-1)
        logits = self.combined_fc(combined_features)
        return logits

    def predict_answer(self, logits):
        probabilities = F.softmax(logits, dim=-1)
        predicted_class = torch.argmax(probabilities, dim=-1)
        return predicted_class, probabilities

if __name__ == '__main__':
    # Dummy data for testing
    batch_size = 4
    input_dim = 10
    hidden_dim = 16
    output_dim = 5
    text_dim = 12
    image_dim = 8

    # Tossup Agent Test
    tossup_agent = ConfidenceCalibratedTossupAgent(input_dim, hidden_dim, output_dim)
    tossup_input = torch.randn(batch_size, input_dim)
    logits, confidence = tossup_agent(tossup_input)
    print("Tossup Agent Logits:", logits)
    print("Tossup Agent Confidence:", confidence)
    decision = tossup_agent.decide_to_answer(confidence, threshold=0.7)
    print("Tossup Agent Decision to Answer:", decision)

    # Bonus Agent Test
    bonus_agent = MultimodalBonusAgent(text_dim, image_dim, hidden_dim, output_dim)
    text_features = torch.randn(batch_size, text_dim)
    image_features = torch.randn(batch_size, image_dim)
    logits = bonus_agent(text_features, image_features)
    print("Bonus Agent Logits:", logits)
    predicted_class, probabilities = bonus_agent.predict_answer(logits)
    print("Bonus Agent Predicted Class:", predicted_class)
    print("Bonus Agent Probabilities:", probabilities)