# from controllers.auth_controller import auth
# from controllers.job_references_controller import job_references
from controllers.auth_controller import auth_bp

registerable_controllers = [
    # job_references_bp,
    auth_bp
]