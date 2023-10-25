class Students:
    def __init__(self,name, course, age , gender,):
        self.name=name
        self.course=course
        self.age=age
        self.gender=gender

    def onyesha(self):
        print("Name: %s \nCourse: %s\nGender: %s\nAge: %d"
              %(self.name, self.course, self.gender, self.age))
