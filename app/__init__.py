from flask import Flask

from app.config import AppConfig
from app.admin.routes import admin_bp
from app.auth.routes import auth_bp
from app.announcements.routes import announcements_bp
from app.dashboard.routes import dashboard_bp
from app.errors import register_error_handlers
from app.exams.routes import exams_bp
from app.imports.routes import imports_bp
from app.leaderboards.routes import leaderboards_bp
from app.logging import configure_logging
from app.mcqs.routes import mcqs_bp
from app.analytics.routes import analytics_bp
from app.achievements.routes import achievements_bp
from app.events.routes import events_bp
from app.results.routes import results_bp
from app.roles.routes import roles_bp
from app.routes import core_bp
from app.subjects.routes import subjects_bp
from app.users.routes import users_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(AppConfig())

    configure_logging(app)
    register_error_handlers(app)

    app.register_blueprint(core_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(announcements_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(subjects_bp)
    app.register_blueprint(mcqs_bp)
    app.register_blueprint(imports_bp)
    app.register_blueprint(exams_bp)
    app.register_blueprint(results_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(leaderboards_bp)
    app.register_blueprint(achievements_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(events_bp)

    return app
