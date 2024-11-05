import spacy
import torch
from torch_geometric.data  import Data
from torch_geometric.nn import GraphConv

# Load resumes and job descriptions
resumes = [...]
job_descriptions = [...]

# Preprocess text data using spaCy
nlp = spacy.load("en_core_web_sm")
resume_embeddings = []
for resume in resumes:
    doc = nlp(resume)
    resume_embeddings.append(doc.vector)

# Create knowledge graph embeddings
kg_embeddings = []
for job_description in job_descriptions:
    doc = nlp(job_description)
    kg_embeddings.append(doc.vector)

# Define graph-based matching model
class GraphMatchingModel(torch.nn.Module):
    def __init__(self):
        super(GraphMatchingModel, self).__init__()
        self.conv1 = GraphConv(128, 128)
        self.conv2 = GraphConv(128, 128)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = torch.relu(x)
        x = self.conv2(x, edge_index)
        return x

# Initialize model and optimizer
model = GraphMatchingModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Train model on resume and job description embeddings
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(resume_embeddings, kg_embeddings)
    loss = torch.mean((outputs - kg_embeddings) ** 2)
    loss.backward()
    optimizer.step()


