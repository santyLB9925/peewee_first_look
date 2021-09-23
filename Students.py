from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):

    username = CharField(max_length=255,unique=True)
    points= IntegerField(default=0)

    class Meta:
        database = db

students=[
    {"username":'aldo',
    "points":3,
    },
    {"username":'pedro',
    "points":8,
    },{"username":'juana',
    "points":7,
    },{"username":'federica',
    "points":9,
    },
    {"username":'paquita',
    "points":5,
    },
]
def add_student():
    for student in students:
        try:

            Student.create(username=student["username"],
                      points=student["points"])
        except IntegrityError:
            student_record=Student.get(username=student["username"])
            student_record.points=student["points"]
            student_record.save()#Actualiza los puntos del estudiante
def get_top_student():
    student=Student.select().order_by(Student.points.desc()).get()
    return student


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student],safe=True) #una vez ejecutado, ya no lo crea
    #add_student()
    print("el mejor estudiante fue: ",get_top_student().username)