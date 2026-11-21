# PSO Hyperparameter Optimization of YOLOv8n (GB-7)

## Overview

This directory contains the Particle Swarm Optimization (PSO) experiments for the BDFD9 textile-defect detection project. The goal was to search for YOLOv8n training hyperparameters using validation performance, retrain a selected model, and evaluate it on the held-out test split.

The experiment code and previously saved results are preserved. Running the notebook is **not required** to review the artifacts and would launch additional model training.

## Dataset and model

- Dataset: cleaned BDFD9 textile defect dataset, with nine defect classes.
- Detector: pretrained Ultralytics YOLOv8n.
- Dataset split: 775 training, 208 validation, and 105 test images.
- Input image size: 640 × 640; batch size: 16.
- Optimizer: AdamW; random seed: 42.

## PSO experiment 2 — configuration

| Setting | Value |
| --- | --- |
| Swarm size | 5 particles |
| PSO iterations | 5 |
| Training epochs per candidate | 10 |
| Inertia weight (w) | 0.6 |
| Cognitive coefficient (c1) | 1.5 |
| Social coefficient (c2) | 1.5 |
| Search variables | Learning rate (`lr0`), momentum, weight decay |
| Fitness objective | Maximize validation mAP50–95 |
| Velocity limit | 20% of each parameter's search-range width |

Each particle represents a candidate set of training hyperparameters. PSO updates particles using their personal best (`pBest`) and the swarm's global best (`gBest`). The experiment includes state saving and reuse of previously evaluated configurations; therefore, the number of unique model evaluations can be less than 25.

### Selected hyperparameters

| Parameter | Selected value |
| --- | ---: |
| Learning rate (`lr0`) | 0.0005596443158499851 |
| Momentum | 0.8602855265995631 |
| Weight decay | 0.0028154436412772326 |

The machine-readable source of these parameters is `results/final_pso_results.json`.

## Final model training and test evaluation

The final experiment-2 training code uses the selected parameters to train a new YOLOv8n model for 50 epochs (`YOLOv8n_PSO_Experiment_2_50_Epochs`). The saved `best.pt` checkpoint from that run was copied to `Deployment_Models/pso_optimized_best.pt` for independent test evaluation.

### Held-out test results

| Metric | Baseline YOLOv8n | PSO-optimized YOLOv8n |
| --- | ---: | ---: |
| Precision | 83.52% | 80.72% |
| Recall | 84.43% | 82.35% |
| mAP50 | 90.09% | 90.35% |
| mAP50–95 | 51.02% | 49.83% |

PSO improved **mAP50 by 0.26 percentage points**, but the baseline achieved higher precision, recall, and mAP50–95. These are test-set results, not the validation fitness values used during PSO search. A higher confidence on a single image is not proof of superior overall detection performance.

## Directory contents

```text
pso_optimization/
├── GB-7_PSO_Optimization.ipynb    # Preserved PSO search and retraining code
├── results/
│   ├── final_pso_results.json      # Selected parameters and final search summary
│   ├── fitness_history.csv         # Recorded particle evaluations
│   ├── pso_state.json              # Saved optimizer state
│   └── PSO_Convergence_Experiment_2.png
├── training_results/              # Final Experiment 2 training curves and validation plots
└── test_results/                  # Independent test-set curves, confusion matrices, examples
```

**Artifact provenance:** `training_results/` contains the corrected final Experiment 2 artifacts from `YOLOv8n_PSO_Experiment_2_50_Epochs` (Git correction commit `22e05eb`). The notebook copies this run's `weights/best.pt` into `Deployment_Models/pso_optimized_best.pt`, and its test-evaluation cell loads that deployment checkpoint with `split="test"`, saving plots in `pso_optimized_best_Test`. The deployment and training checkpoints were verified to have identical SHA256 hashes.

## Reproduction notes

1. Install PyTorch with appropriate CUDA support, Ultralytics, NumPy, pandas, matplotlib, and PyYAML.
2. Prepare the cleaned BDFD9 dataset and update the local dataset paths in the notebook.
3. Run the PSO search only if a new search is needed; each uncached candidate trains a YOLO model for 10 epochs.
4. Use `final_pso_results.json` to retrieve the selected hyperparameters.
5. Retrain YOLOv8n for 50 epochs using the selected parameters, then evaluate the resulting `best.pt` on the test split.

**Note:** Model weights and the individual particle-training folders are not included in this directory. Existing saved figures and CSV/JSON files can be reviewed without running training.
