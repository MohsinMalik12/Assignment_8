import mongoengine

class StudentData(mongoengine.Document):
    student_ID = mongoengine.IntField(required=True)
    student_name = mongoengine.StringField(required=True)
    student_father_name = mongoengine.StringField(required=True)
    student_gender = mongoengine.StringField(required=True)
    student_age = mongoengine.IntField(required=True)
    student_marks = mongoengine.IntField(required=True)

    def __str__(self):
        return self.student_name