"""
Configuration file for all hyperparameters
"""

CONFIG = {
    # Model architecture
    'model': {
        'd_model': 256,          # Embedding dimension
        'n_heads': 8,            # Number of attention heads
        'n_layers': 6,           # Number of transformer blocks
        'd_ff': 1024,            # Feedforward hidden dimension
        'dropout': 0.1,          # Dropout probability
        'max_seq_len': 200,      # Maximum sequence length
        'vocab_size': 70         # 64 cards + 4 categories + 2 special tokens
    },
    
    # Training parameters
    'training': {
        'batch_size': 32,
        'learning_rate': 3e-4,
        'weight_decay': 0.01,
        'epochs': 100,
        'warmup_steps': 1000,
        'grad_clip': 1.0,
        'patience': 15           # Early stopping patience
    },
    
    # Data generation
    'data': {
        'train_size': 10000,
        'val_size': 2000,
        'test_size': 2000,
        'min_context_trials': 1,
        'max_context_trials': 5,
        'switch_probability': 0.3  # Probability of rule change
    },
    
    # Paths
    'paths': {
        'checkpoint_dir': './checkpoints/',
        'plot_dir': './plots/',
        'log_dir': './logs/',
        'data_dir': './data/'
    },
    
    # Random seed for reproducibility
    'seed': 42
}
