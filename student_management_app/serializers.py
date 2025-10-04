from rest_framework import serializers

class StaffSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    address = serializers.CharField(allow_blank=True, required=False)

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    course_name = serializers.CharField()
    course_description = serializers.CharField(allow_blank=True, required=False)

class SessionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    session_name = serializers.CharField()

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    course_id = serializers.IntegerField()
    session_id = serializers.IntegerField()

class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject_name = serializers.CharField()
    course_id = serializers.IntegerField()

class AttendanceItemSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    status = serializers.ChoiceField(choices=['present','absent','late'])

class AttendanceSerializer(serializers.Serializer):
    subject_id = serializers.IntegerField()
    attendance_date = serializers.DateField()
    attendance = AttendanceItemSerializer(many=True)

class LeaveSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    leave_date = serializers.DateField()
    leave_message = serializers.CharField()
    status = serializers.CharField(required=False)

class FeedbackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    message = serializers.CharField()
    reply = serializers.CharField(required=False)
