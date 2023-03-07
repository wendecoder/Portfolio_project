import os
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    
    @app.route('/')
    def index():
        return "hellooh"

    #after request decorator to specify the headers and allowed methods

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    #app decorator to list available categories.

    @app.route('/categories', methods=['GET'])
    def avail_categories():
        try:
            res = Category.query.all()
            tempdict = {}
            i = len(res)
            for n in range(i):
                temp1 = {
                    res[n].id: res[n].type
                }
                tempdict.update(temp1)
            
            return jsonify({
                'success': True,
                'categories': tempdict
                })
        except:
            abort(404)

    #method and app decorator to list questions paginated.

    def paginate_questions(request, options):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        questions = [question.format() for question in options]
        current_questions = questions[start:end]
        return current_questions

    @app.route('/questions', methods=['GET'])
    def retrieve_questions():
        try:
            res = Category.query.all()
            tempdict = {}
            i = len(res)
            for n in range(i):
                temp1 = {
                    res[n].id: res[n].type
                }
                tempdict.update(temp1)
            page = request.args.get('page', 1, type=int)
            start = (page - 1) * QUESTIONS_PER_PAGE
            options = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, options)
            catid = options[start].category
            current_category = Category.query.get(catid)
            if len(current_questions) == 0:
                abort(404)
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(Question.query.all()),
                'current_category': current_category.type,
                'categories': tempdict
            })
        except:
            abort(404)    

    #app decorator to delete a question using the id of the question.

    @app.route('/questions/<int:questions_id>', methods=['DELETE'])
    def delete_questions(questions_id):
        try:
            question = Question.query.get(questions_id)

            if question is None:
                abort(404)
            question.delete()
            options = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, options)

            return jsonify({
                'success': True,
                'question_deleted': questions_id,
                'current_questions': current_questions,
                'total_questions': len(Question.query.all())
            })
        except:
            abort(400)

    #app decorator to add new questions and to search for a question with specific term.

    @app.route('/questions', methods=['POST'])
    def create_question():

        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        search_term = body.get('searchTerm', None)
        if search_term is not None:
            questions = Question.query.filter(Question.question.ilike("%"+search_term+"%")).all()
            if len(questions) == 0:
                abort(404)
            try:  
                formatted_questions = [question.format() for question in questions]
                category = questions[0].category
                currenCategory = Category.query.get(category)
                return jsonify({
                    "success": True,
                    "questions": formatted_questions,
                    "totalQuestions": len(formatted_questions),
                    "currentCategory": currenCategory.type
                    }
                )
            except:
                abort(422)

        else:
            try:
                question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
                question.insert()

                options = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, options)

                return jsonify({
                    'success': True,
                    'created_question': question.id,
                    'questions': current_questions,
                    'total_questions': len(Question.query.all())
                })
            except:
                abort(405)
   
    
    #app decorator to get questions by category

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_by_category(category_id):
        questions = Question.query.filter(Question.category == category_id).all()
        
        if len(questions) == 0:
                abort(404)
        try:
            currcat = Category.query.get(category_id)
            formatted_questions = [question.format() for question in questions]
            return jsonify({
                "success": True,
                "questions": formatted_questions,
                "totalQuestions": len(formatted_questions),
                "currentCategory": currcat.type
            })
        except:
            abort(422)
    
    #app decorator for quizz play
    
    @app.route('/quizzes', methods=['POST', 'GET'])
    def play_quizz():
        #try:
            body = request.get_json()
            previous_question = body.get('previous_questions', None)
            quiz_category = body['quiz_category']
            if quiz_category['id'] == 0:
                categories = Category.query.all()
                random.shuffle(categories)
                categories_id = categories[0].id
                questions = Question.query.filter(Question.category == categories_id).all()
                i = len(categories)
                toggle = False
                for n in range(i):
                    if questions[n].id not in previous_question:
                        quiz_question = questions[n]
                        toggle = True
                        break
            
                if toggle:
                    quiz_question_formatted = quiz_question.format()
                if toggle is False:
                    quiz_question_formatted = {}
            else: 
                categories = Category.query.filter(Category.type == quiz_category['type']).first()
                questions = Question.query.filter(Question.category == categories.id).all()
                random.shuffle(questions)
                i = len(questions)
                toggle = False
                for n in range(i):
                    if questions[n].id not in previous_question:
                        quiz_question = questions[n]
                        toggle = True
                        break
            
                if toggle:
                    quiz_question_formatted = quiz_question.format()
                if toggle is False:
                    quiz_question_formatted = {}        
            return jsonify({
                "success": True,
                "question": quiz_question_formatted
            })         
        #except:
            abort(422)


    #error handler decorators for all errors that are thrown by each endpoint
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "message": "Resource not found",
            "error": 404
        }), 404
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "message": "couldn't be processed",
            "error": 422
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "message": "bad_request",
            "error": 400
        }), 400
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "message": "Method not allowed",
            "error": 405
        }), 405
    return app

