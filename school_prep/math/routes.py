from flask import Blueprint, render_template, request, jsonify, make_response, Markup
from flask_paginate import Pagination, get_page_args, get_page_parameter
from ..MathUtils.MathAddition import Addition


math = Blueprint('math', __name__)


@math.route('/math/addition', methods=["GET", 'POST'])
def math_addition():
    return render_template("addition.html")


@math.route('/math/addition/start', methods=["GET", 'POST'])
def math_addition_problem():
    math_addition_problems = list(Addition(10).generate_addition_problems())

    page, per_page, offset = get_page_args(page_parameter='problem',
                                           per_page_parameter='per_page')
    total = len(math_addition_problems)
    pagination_users = get_addition_problems(math_addition_problems, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template('addition_problem.html',
                           problems=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


def question_qty():
    return int(request.form['add_questions'])


def get_addition_problems(math_problem, offset=0, per_page=10):
    return math_problem[offset: offset + per_page]
