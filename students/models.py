from django.db import models

# Create your models here.

class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=20)
    class_short_form = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Class List'

    def __str__(self):
        return self.class_name


class StudentSectionInfo(models.Model):
    section_name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Section List'

    def __str__(self):
        return self.section_name


class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Shift List'

    def __str__(self):
        return self.shift_name
class StudentInfo(models.Model):
    academic_year  = models.CharField(max_length=100)
    admission_date = models.DateField()
    admission_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    class_type = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    section_type = models.ForeignKey(StudentSectionInfo, on_delete=models.CASCADE)
    shift_type = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    # student_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fathers_name = models.CharField(max_length=100)
    # fathers_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fathers_nid = models.IntegerField(unique=True)
    fathers_number = models.IntegerField(unique=True)
    mothers_name = models.CharField(max_length=100)
    # mothers_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    mothers_nid = models.IntegerField(unique=True)
    mothers_number = models.IntegerField()
    class Meta:
        # unique_together = ["admission_id", "class_type"]
        verbose_name_plural = 'Student List'

    def __str__(self):
        return self.name