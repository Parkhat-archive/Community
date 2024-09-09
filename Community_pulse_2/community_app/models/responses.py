from community_app import db


class Responses(db.Model):
    __tablename__ = 'responses'
    id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable= False)
    is_agree = db.Column(db.Boolean, nullable = False)


    def __str__(self):
        return f'Questions_id: {self.question_id}, Answer: {self.is_agree}'

