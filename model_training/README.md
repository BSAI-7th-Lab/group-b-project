\# Baseline YOLOv8n Model Training and Evaluation



\## Project Overview



This module implements a baseline YOLOv8n object detection model for industrial textile defect detection using the BDFD9 dataset. The baseline establishes a reference for evaluating the effectiveness of Particle Swarm Optimization (PSO) in hyperparameter optimization.



\*\*Jira Task:\*\* GB-2 — Baseline YOLOv8n Model Training and Validation



\## 1. Dataset



The BDFD9 Bangladesh Centric Fabric Defect Dataset contains nine textile defect classes.



| Dataset Split | Images |

|---|---:|

| Training | 775 |

| Validation | 208 |

| Testing | 105 |

| Total | 1088 |



\### Defect Classes



\- DropStitch

\- Hole

\- Horizontal Mark

\- Knot

\- Oil Spot

\- Setup

\- Slub

\- Vertical LineMark

\- Yurn Dust



\## 2. Training Configuration



The pretrained YOLOv8n model was trained using the following configuration:



| Parameter | Value |

|---|---|

| Model | YOLOv8n |

| Epochs | 50 |

| Image Size | 640 × 640 |

| Batch Size | 16 |

| Optimizer | AdamW |

| Learning Rate | 0.001 |

| Momentum | 0.9 |

| Weight Decay | 0.0005 |

| Random Seed | 42 |

| Hardware | NVIDIA GeForce RTX 3090 (24 GB) |



\## 3. Model Performance



| Evaluation Metric | Validation | Test |

|---|---:|---:|

| Precision | 87.70% | 83.52% |

| Recall | 80.00% | 84.43% |

| mAP@50 | 89.70% | 90.09% |

| mAP@50–95 | 45.10% | 51.02% |



The baseline model achieved a test mAP@50 of 90.09%, establishing a reference for subsequent PSO-based optimization.



\## 4. Training and Validation Results



The training and validation results include epoch-wise statistics, loss curves, performance curves, confusion matrices, and sample predictions.



\### Training Performance



!\[Training Results](results/results.png)



\### Validation Confusion Matrix



!\[Validation Confusion Matrix](results/confusion\_matrix.png)



\### Validation Precision-Recall Curve



!\[Validation PR Curve](results/BoxPR\_curve.png)



\## 5. Test Evaluation Results



The baseline model was evaluated on the separate test dataset to assess its generalization performance.



\### Test Confusion Matrix



!\[Test Confusion Matrix](test\_results/confusion\_matrix.png)



\### Test Precision-Recall Curve



!\[Test PR Curve](test\_results/BoxPR\_curve.png)



\### Sample Test Predictions



!\[Test Predictions](test\_results/val\_batch0\_pred.jpg)



\## 6. Repository Structure



```text

model\_training/

├── YOLOv8n\_Baseline.ipynb

├── results/

│   ├── args.yaml

│   ├── baseline\_metrics.json

│   ├── results.csv

│   ├── results.png

│   ├── Performance curves

│   ├── Confusion matrices

│   └── Validation sample predictions

├── test\_results/

│   ├── Performance curves

│   ├── Confusion matrices

│   └── Test sample predictions

└── README.md

```



\## 7. Reproducibility



The notebook preserves the original training outputs. Dataset paths and model checkpoint paths must be configured according to the local environment before execution. The model weights are not included in this directory.



\## 8. Next Phase



The baseline results will be used to evaluate PSO-based hyperparameter optimization of learning rate, momentum, and weight decay under a consistent final training and evaluation setup.



\## 9. Conclusion



The baseline YOLOv8n model has been trained, validated, and evaluated on the BDFD9 dataset. The training notebook, configuration, performance metrics, and evaluation visualizations are organized for future comparison with the PSO-optimized model.

