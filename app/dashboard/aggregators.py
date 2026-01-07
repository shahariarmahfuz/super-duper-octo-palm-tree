def summarize_dashboard(metrics: dict) -> dict:
    return {
        "total_subjects": metrics.get("subjects", 0),
        "total_mcqs": metrics.get("mcqs", 0),
        "total_attempts": metrics.get("attempts", 0),
        "accuracy": metrics.get("accuracy", 0),
    }
