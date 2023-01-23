from django import forms

class AttendanceForm(forms.Form):
    ATTENDANCE_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Excused', 'Excused'),
    )
    attendance = forms.ChoiceField(choices=ATTENDANCE_CHOICES)