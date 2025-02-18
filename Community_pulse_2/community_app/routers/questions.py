from flask import Blueprint,jsonify, request, make_response
from pydantic import ValidationError

from community_app.models.questions import Questions
from community_app import db
from community_app.schemas.questions import QuestionCreate, QuestionResponse



questions_bp = Blueprint('questions', __name__, url_prefix = '/questions')

@questions_bp.route('/',  methods = ['GET'])
def get_all_questions():
    questions: list[Questions] = Questions.query.all()

    result = [QuestionResponse.from_orm(question).dict() for question in questions ]

    response = make_response(jsonify(result), 200)
    return response


    # questions_data: list[dict] = [
    #     {
    #         "id": question.id,
    #         "text": question.text,
    #         "created_at": question.created_at
    #     }
    #     for question in questions]
    # response = make_response(jsonify(questions_data), 200)
    # #response.headers["Custom-Header"] = "our custom header"

    # return response



@questions_bp.route('/add', methods = ['POST'])
def add_new_questions():
    data = request.get_json()
    try:
        question_data = QuestionCreate(**data)
    except ValidationError as err:
        return make_response(jsonify(err.errors()), 400)

    question : Questions = Questions(text = question_data.text)
    db.session.add(question)
    db.session.commit()

    return make_response(jsonify(QuestionResponse(
        id = question.id,
        text = question.text).dict()), 201)



    # if not data or 'text' not in data:
    #     return  jsonify(
    #         {
    #             'message': 'NO DATA PROVIDED'
    #         }
    #     ), 400
    # question: Questions = Questions(text = data['text'])
    # db.session.add(question)
    # db.session.commit()

    # return jsonify(
    #     {
    #         "message": "NEW QUESTION added",
    #         "question_id" : question.id
    #     }
    # ), 201


@questions_bp.route('update/<int:id>', methods=['PUT'])
def update_question(id):
    """Обновление конкретного вопроса по его ID."""
    question = Questions.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404

    data = request.get_json()
    if 'text' in data:
        question.text = data['text']
        db.session.commit()
        return jsonify({'message': f"Вопрос обновлен: {question.text}"}), 200
    else:
        return jsonify({'message': "Текст вопроса не предоставлен"}), 400


@questions_bp.route('delete/<int:id>', methods=['DELETE'])
def delete_question(id):
    """Удаление конкретного вопроса по его ID."""
    question = Questions.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404

    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': f"Вопрос с ID {id} удален"}), 200