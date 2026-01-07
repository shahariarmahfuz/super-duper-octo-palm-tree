from app.dashboard.aggregators import summarize_dashboard
from app.dashboard.presenters import format_metric
from app.dashboard.repository import fetch_dashboard_metrics


def build_dashboard_snapshot() -> dict:
    metrics = fetch_dashboard_metrics()
    summary = summarize_dashboard(metrics)
    return {key: format_metric(value) for key, value in summary.items()}
