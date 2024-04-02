# mlplatform_k8s
### This repo provides YAML files for creating MLplatform based on k8s and contains:
1. yaml files for setting up kind cluster and necessary structures
    - minio s3 storage
    - mlflow platform
    - single-user juputerlab with authentication by token
2. ansible playbook yaml for localhost deploying:
    - installation requires that yaml files already on host and located in /home/neo/project2 directory
    - installation requires that kind utility already installed on host
  
