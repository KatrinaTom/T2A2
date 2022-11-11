
@job_bp.route('/<int:user_id>/job', methods=['POST'])
def create_job(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalars(stmt)
    if user:
        create_job =  Job(
            user_id = request.json['user_id'],
            status = request.json['status'],
            start_date = request.json['start_date'],
            end_date = request.json['end_date'],
            units_hours = request.json['units_hours'],
            description = request.json['description'],
        )
        db.session.add(create_job)
        db.session.commit()
        return JobSchema().dump(job_product), 201
    else:
        return{'error': f'{user_id} not found to create the job'}, 404