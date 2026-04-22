# LLM Coding Evaluation Framework

A lightweight framework for evaluating the coding ability of small LLMs using automated unit test execution.

## What it does
- Prompts a causal LLM with Python coding tasks
- Extracts and executes the generated code
- Runs unit tests and reports pass@1

## Models
Qwen/Qwen2.5-0.5B-Instruct  
Qwen/Qwen2.5-1.5B-Instruct

## Results

| Model | pass@1 | strings | math | lists | algorithms | dicts |
|-------|--------|---------|------|-------|------------|-------|
| Qwen2.5-0.5B-Instruct | 60.00% | 3/5 | 4/5 | 4/5 | 1/3 | 0/2 |
| Qwen2.5-1.5B-Instruct | 95.00% | 5/5 | 5/5 | 5/5 | 3/3 | 1/2 |

### Key findings
- 1.5B model achieves near-perfect pass@1 (95%) vs 60% for 0.5B
- Largest gap in algorithms category (33% vs 100%)
- Dict-related tasks remain challenging even for the larger model

## Setup
```bash
pip install transformers torch
python3 evaluate.py
```

## Project Structure
- `tasks.py` — coding tasks and unit tests
- `model.py` — model loading and text generation
- `evaluate.py` — evaluation loop and metrics
