from flask import Blueprint, render_template, request, jsonify
from flask_paginate import Pagination, get_page_args, get_page_parameter
from ..MathUtils.MathAddition import Addition

test = Blueprint('test', __name__)


def get_users(users, offset=0, per_page=10):
    return users[offset: offset + per_page]


@test.route('/pag/test', methods=["GET", 'POST'])
def pag_test():
    users = list(Addition(5).generate_addition_problems())

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(users, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('test.html',
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


