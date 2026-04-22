import json
import re
import torch
from model import load_model, generate_code
from tasks import TASKS

MODELS = [
    "Qwen/Qwen2.5-0.5B-Instruct",
    "Qwen/Qwen2.5-1.5B-Instruct",
]

def extract_code(response):
    response = re.sub(r"```python\n?", "", response)
    response = re.sub(r"```\n?", "", response)
    return response.strip()


def run_test(code, test):
    """
    Izvrsava kod + unit test u izolovanom namespace-u.
    Vraca (passed: bool, error: str | None)
    """
    namespace = {}
    
    try:
        exec(code, namespace)
    except Exception as e:
        return False, f"Code execution error: {e}"
    
    try:
        exec(test, namespace)
        return True, None
    except AssertionError:
        return False, "Assertion failed"
    except Exception as e:
        return False, f"Test error: {e}"


def evaluate():
    all_results = {}

    for model_name in MODELS:
        tokenizer, model, device = load_model(model_name)
        results = []
        passed = 0

        for task in TASKS:
            print(f"\n[{model_name}] Task {task['id']}: {task['prompt'][:50]}...")
            response = generate_code(task["prompt"], tokenizer, model, device)
            code = extract_code(response)
            success, error = run_test(code, task["test"])

            if success:
                passed += 1
                print(f"PASSED")
            else:
                print(f"FAILED - {error}")

            results.append({
                "task_id": task["id"],
                "prompt": task["prompt"],
                "generated_code": code,
                "passed": success,
                "error": error
            })

        pass_at_1 = passed / len(TASKS)

        categories = {}
        for r in results:
            task = next(t for t in TASKS if t["id"] == r["task_id"])
            cat = task["category"]
            if cat not in categories:
                categories[cat] = {"passed": 0, "total": 0}
            categories[cat]["total"] += 1
            if r["passed"]:
                categories[cat]["passed"] += 1

        all_results[model_name] = {
            "passed": passed,
            "total": len(TASKS),
            "pass_at_1": pass_at_1,
            "categories": categories,
            "results": results
        }

        del model
        import gc
        gc.collect()
        if device == "mps":
            torch.mps.empty_cache()

    
    print()
    print(f"{'Model':<35} {'pass@1':<10} {'strings':<10} {'math':<10} {'lists':<10} {'algorithms':<12} {'dicts'}")
    for m, r in all_results.items():
        name = m.split("/")[-1]
        cats = r["categories"]
        print(f"{name:<35} {r['pass_at_1']:<10.2%} "
              f"{cats['strings']['passed']}/{cats['strings']['total']:<8} "
              f"{cats['math']['passed']}/{cats['math']['total']:<8} "
              f"{cats['lists']['passed']}/{cats['lists']['total']:<8} "
              f"{cats['algorithms']['passed']}/{cats['algorithms']['total']:<10} "
              f"{cats['dicts']['passed']}/{cats['dicts']['total']}")

    with open("results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"\nResults saved to results.json")


if __name__ == "__main__":
    evaluate()