from flask import Blueprint

from app.controllers.GroupController import index, store, show, update, delete

bp = Blueprint('group', __name__)

bp.route('/', methods=['GET'])(index)
bp.route('/create', methods=['POST'])(store)
bp.route('/<string:id>', methods=['GET'])(show)
bp.route('/<string:id>/edit', methods=['POST'])(update)
bp.route('/<string:id>', methods=['DELETE'])(delete)
