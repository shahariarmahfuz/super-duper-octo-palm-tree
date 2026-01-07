from flask import Blueprint, jsonify

from app.analytics.services import (
    build_cohort_analysis,
    build_growth_trends,
    build_question_analysis,
    build_subject_analysis,
)

analytics_bp = Blueprint("analytics", __name__, url_prefix="/analytics")


@analytics_bp.get("/subjects")
def subject_analytics():
    return jsonify({"subjects": build_subject_analysis()})


@analytics_bp.get("/questions")
def question_analytics():
    return jsonify({"questions": build_question_analysis()})


@analytics_bp.get("/cohorts")
def cohort_analytics():
    return jsonify({"cohorts": build_cohort_analysis()})


@analytics_bp.get("/trends")
def trend_analytics():
    return jsonify({"trends": build_growth_trends()})
