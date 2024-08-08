from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    all_assignments = Assignment.get_assignments_all()
    all_assignments_dump = AssignmentSchema().dump(all_assignments, many=True)
    return APIResponse.respond(data=all_assignments_dump)

@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    
    graded_assignment = Assignment.get_by_id(grade_assignment_payload.id)
    
    if graded_assignment.state == "DRAFT":
        return APIResponse.respond(data={"message":"Cannot grade an assignment in Draft state"},status_code=400)
    
    else:
        graded_assignment = Assignment.mark_grade(
            _id=graded_assignment.id,
            grade=grade_assignment_payload.grade,
            auth_principal=p
        )
        regraded_assignment = Assignment.regrade(
            _id=graded_assignment.id,
            grade=grade_assignment_payload.grade,
            auth_principal=p
        )
        db.session.commit()
        regraded_assignment_dump = AssignmentSchema().dump(regraded_assignment)
        return APIResponse.respond(data=regraded_assignment_dump)