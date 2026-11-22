"""GB-9: Reproduce the baseline vs PSO comparison from documented test metrics.

Inputs are percentages transcribed from model_training/README.md and
pso_optimization/README.md; no model inference or training is performed.
"""
from pathlib import Path
import csv
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
METRICS = [
    ('Precision', 83.52, 80.72),
    ('Recall', 84.43, 82.35),
    ('mAP@50', 90.09, 90.35),
    ('mAP@50-95', 51.02, 49.83),
]

with (OUT / 'comparison_metrics.csv').open('w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['metric', 'baseline_percent', 'pso_optimized_percent', 'pso_minus_baseline_percentage_points'])
    for metric, baseline, pso in METRICS:
        writer.writerow([metric, f'{baseline:.2f}', f'{pso:.2f}', f'{pso-baseline:+.2f}'])

fig, ax = plt.subplots(figsize=(9, 5.4))
x = list(range(len(METRICS)))
width = 0.36
left = ax.bar([i - width / 2 for i in x], [r[1] for r in METRICS], width, label='Baseline YOLOv8n')
right = ax.bar([i + width / 2 for i in x], [r[2] for r in METRICS], width, label='PSO-optimized YOLOv8n')
ax.set_xticks(x, [r[0] for r in METRICS])
ax.set_ylim(0, 105)
ax.set_ylabel('Test-set score (%)')
ax.set_title('BDFD9: Baseline vs PSO-optimized YOLOv8n')
ax.legend(loc='lower left')
ax.grid(axis='y', alpha=0.2)
ax.set_axisbelow(True)
for bars in (left, right):
    ax.bar_label(bars, fmt='%.2f', padding=3, fontsize=9)
fig.tight_layout()
fig.savefig(OUT / 'performance_comparison.png', dpi=180)
plt.close(fig)
print('Created comparison_metrics.csv and performance_comparison.png')
