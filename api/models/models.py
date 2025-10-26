from pydantic import BaseModel

class ModelRequest(BaseModel):
    model_name: str
    ecr_uri: str # Example: "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-model:latest"  
    search_method: str # Example: "grid_search" or "random_search"
    dataset_s3_uri: str # Example: "s3://my-bucket/datasets/my-dataset.csv"
    serach_space: dict # Example: {"learning_rate": [0.01, 0.1, 0.2], "batch_size": [16, 32, 64]}
    static_parameters: dict # Example: {"epochs": 10, "optimizer": "adam"}
    budget: int # Example: 5 (number of training jobs to run)
    objective_metric: str # Example: "accuracy"