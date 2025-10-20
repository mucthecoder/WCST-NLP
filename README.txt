WCST Transformer Implementation
================================

This project implements a transformer model from scratch to solve the 
Wisconsin Card Sorting Test (WCST), a neuropsychological test of cognitive flexibility.

Project Structure
-----------------
.
├── config.py                  # Hyperparameter configuration
├── data_generator.py          # WCST data generation and preprocessing
├── model.py                   # Transformer architecture implementation
├── train.py                   # Training loop and optimization
├── evaluate.py                # Evaluation metrics and analysis
├── analysis.py                # Mechanistic interpretability analysis
├── scaling_experiments.py     # Scaling law experiments
├── main.py                    # Main entry point
├── utils.py                   # Utility functions
├── wcst.py                    # Provided WCST data generator (DO NOT SUBMIT)
├── requirements.txt           # Python dependencies
├── README.txt                 # This file
│
├── checkpoints/               # Saved model weights
├── plots/                     # Generated visualizations
├── logs/                      # Training logs
├── data/                      # Generated datasets (optional)
└── notebooks/                 # Jupyter notebooks for exploration (optional)

Getting Started
---------------
1. Install dependencies:
   pip install -r requirements.txt

2. Place the provided wcst.py file in the project root directory

3. Run the full pipeline:
   python main.py

4. Or run individual components:
   python train.py              # Training only
   python evaluate.py           # Evaluation only
   python analysis.py           # Interpretability analysis

File Descriptions
-----------------
config.py:
    Central configuration file containing all hyperparameters for the model,
    training, and data generation. Modify this to tune the model.

data_generator.py:
    Wraps the WCST class to generate training, validation, and test datasets.
    Handles sequence creation with multiple trials and context switches.

model.py:
    Complete transformer implementation from scratch including:
    - Token and positional embeddings
    - Multi-head self-attention
    - Feed-forward networks
    - Transformer blocks
    - Full model architecture

train.py:
    Training loop with:
    - Loss computation (cross-entropy on answer tokens)
    - Optimization (AdamW with warmup)
    - Validation
    - Early stopping
    - Checkpointing

evaluate.py:
    Comprehensive evaluation including:
    - Overall accuracy
    - Accuracy by feature type (color/shape/quantity)
    - Context switch analysis
    - Perseverative error measurement

analysis.py:
    Mechanistic interpretability analysis:
    - Embedding visualizations (PCA/t-SNE)
    - Attention pattern analysis
    - Induction head detection
    - Ablation studies

scaling_experiments.py:
    Experiments to test:
    - Scaling laws (model size vs performance)
    - In-context learning emergence
    - Dataset size effects

main.py:
    Orchestrates the entire pipeline from data generation through
    training, evaluation, and analysis.

utils.py:
    Common utility functions for checkpointing, plotting, etc.

Expected Outputs
----------------
After running the pipeline, you should see:

checkpoints/:
    - best_model.pt            # Best model based on validation loss
    - checkpoint_epoch_X.pt    # Regular checkpoints

plots/:
    - training_curves.png      # Loss and accuracy over time
    - embedding_visualization.png
    - attention_patterns.png
    - induction_heads.png
    - ablation_study.png
    - (and more)

logs/:
    - training.log             # Detailed training logs

Notes
-----
- Training requires a GPU for reasonable speed (2-4 hours on single GPU)
- Adjust batch_size in config.py if running out of GPU memory
- Set 'seed' in config.py for reproducible results
- The model learns to identify sorting rules from context alone

Troubleshooting
---------------
If training is unstable:
    - Reduce learning_rate in config.py
    - Increase grad_clip
    - Add more dropout

If model isn't learning:
    - Check data generation (print some examples)
    - Verify causal masking is correct
    - Try simpler architecture (fewer layers/heads)

If out of memory:
    - Reduce batch_size
    - Reduce d_model or n_layers
    - Reduce max_seq_len

For Submission
--------------
Submit:
    ✓ All .py files (except wcst.py)
    ✓ requirements.txt
    ✓ README.txt (this file)
    ✓ report.pdf (6 pages, IEEE format, with ethics statement)

Do NOT submit:
    ✗ wcst.py (this was provided)
    ✗ checkpoints/ directory
    ✗ plots/ directory
    ✗ logs/ directory
    ✗ data/ directory

Academic Integrity
------------------
- Code must be your own implementation
- Using ChatGPT for code is NOT permitted (plagiarism)
- Using ChatGPT for writing the report IS permitted
- Check your code against the tutorial to ensure it's not identical

Contact
-------
For questions, refer to:
- Course Moodle page
- Office hours
- Course forum

Good luck!
