import json
import re
from model import load_model, generate_code
from tasks import TASKS


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
    tokenizer, model, device = load_model()
    
    results = []
    passed = 0

    for task in TASKS:
        print(f"\nTask {task['id']}: {task['prompt'][:50]}...")
        
        response = generate_code(task["prompt"], tokenizer, model, device)
        code = extract_code(response)
        success, error = run_test(code, task["test"])
        
        if success:
            passed += 1
            print(f"PASSED")
        else:
            print(f"FAILED — {error}")
            print(f"Generated code:\n{code}\n")
        
        results.append({
            "task_id": task["id"],
            "prompt": task["prompt"],
            "generated_code": code,
            "passed": success,
            "error": error
        })

    pass_at_1 = passed / len(TASKS)
    print()
    print(f"Results: {passed}/{len(TASKS)} passed")
    print(f"pass@1: {pass_at_1:.2%}")
    
    with open("results.json", "w") as f:
        json.dump({
            "model": "Qwen/Qwen2.5-0.5B-Instruct",
            "total_tasks": len(TASKS),
            "passed": passed,
            "pass_at_1": pass_at_1,
            "results": results
        }, f, indent=2)
    
    print(f"Results saved to results.json")


if __name__ == "__main__":
    evaluate()