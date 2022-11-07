from controllers.job_reference_controller import job_reference_bp
from controllers.auth_controller import auth_bp
from controllers.service_controller import service_bp

registerable_controllers = [
    job_reference_bp,
    auth_bp,
    service_bp
]