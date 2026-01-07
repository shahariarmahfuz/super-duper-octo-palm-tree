def score_answers(answers: list[dict]) -> dict:
    correct = sum(1 for answer in answers if answer.get("correct"))
    total = len(answers)
    accuracy = (correct / total) * 100 if total else 0
    return {"correct": correct, "total": total, "accuracy": accuracy}
