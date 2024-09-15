from rest_framework import serializers
from .models import StudentData

class StudentDataSerializer(serializers.Serializer):
    student_ID = serializers.IntegerField(read_only=True)
    student_name = serializers.CharField(max_length=200)
    student_father_name = serializers.CharField(max_length=100)
    student_gender = serializers.CharField()
    student_age = serializers.IntegerField()
    student_marks = serializers.IntegerField()

    def create(self, validated_data):
        return StudentData(**validated_data).save()

    def update(self, instance, validated_data):
        instance.student_ID = validated_data.get('student_ID', instance.student_ID)
        instance.student_name = validated_data.get('student_name', instance.student_name)
        instance.student_father_name = validated_data.get('student_father_name', instance.student_father_name)
        instance.student_gender = validated_data.get('student_gender', instance.student_gender)
        instance.student_age = validated_data.get('student_age', instance.student_age)
        instance.student_marks = validated_data.get('student_marks', instance.student_marks)
        instance.save()
        return instance