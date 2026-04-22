# LLM Coding Evaluation Framework

A lightweight framework for evaluating the coding ability of small LLMs using automated unit test execution.

## What it does
- Prompts a causal LLM with Python coding tasks
- Extracts and executes the generated code
- Runs unit tests and reports pass@1

## Model
Qwen/Qwen2.5-0.5B-Instruct

## Results
| Model | Tasks | pass@1 |
|-------|-------|--------|
| Qwen2.5-0.5B-Instruct | 5 | 80.00% |

## Setup
```bash
pip install transformers torch
python3 evaluate.py
```

## Project Structure
- `tasks.py` — coding tasks and unit tests
- `model.py` — model loading and text generation
- `evaluate.py` — evaluation loop and metrics