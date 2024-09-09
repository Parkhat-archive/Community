from datetime import datetime

from community_app import db


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    responses = db.relationship('Responses', backref = 'question', lazy=True)

    def __str__(self):
        return f'Questions: {self.text}'


class Statistics(db.Model):
    __tablename__ = 'statistics'
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key = True)
    agree_count = db.Column(db.Integer, nullable=False, default = 0)
    disagree_count = db.Column(db.Integer, nullable=False, default = 0)

    def __str__(self):
        return f'Statistics for question # {self.question_id}: agreed: {self.agree_count}, disagreed: {self.disagree_count}'