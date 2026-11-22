# GB-9 — Baseline vs PSO-Optimized YOLOv8n

## Objective
Compare the baseline and PSO-optimized YOLOv8n models for textile defect detection on the same held-out BDFD9 test split (105 images).

## Test results

| Metric | Baseline | PSO optimized | PSO − baseline |
|---|---:|---:|---:|
| Precision | 83.52% | 80.72% | −2.80 percentage points |
| Recall | 84.43% | 82.35% | −2.08 percentage points |
| mAP@50 | 90.09% | 90.35% | +0.26 percentage points |
| mAP@50–95 | 51.02% | 49.83% | −1.19 percentage points |

**Interpretation:** PSO produced a small gain in mAP@50 but lower precision, recall, and mAP@50–95. These single-run results do not establish a consistent overall improvement. No statistical significance claim is made.

## Reproduce comparison outputs

Run from the project root:

```bash
python model_comparison/compare_models.py
```

Requires `matplotlib`. The script does **not** retrain or reevaluate the models; it plots and tabulates the previously documented independent-test metrics.

## Files

- `compare_models.py`: reproducible comparison generator
- `comparison_metrics.csv`: test scores and differences in percentage points
- `performance_comparison.png`: grouped bar chart
- `README.md`: methods, findings, and limitations

## Provenance

The numerical inputs are transcribed from `model_training/README.md` and `pso_optimization/README.md` in this repository. The saved test visualization artifacts are in `model_training/test_results/` and `pso_optimization/test_results/`. The PSO deployment checkpoint was independently confirmed by matching SHA256 hashes to the final Experiment 2 training `best.pt` checkpoint. This comparison does not independently recompute scores from predictions.

## Limitations

- Metrics are taken from documented single-run test evaluations, not aggregated over repeated seeds.
- Class-wise quantitative comparisons are not included because a class-wise metrics table was not verified from the available records.
- The small mAP@50 gain should not be interpreted as a statistically reliable improvement without repeated experiments.
