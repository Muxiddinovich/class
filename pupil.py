class Pupil:
    def __init__(self, first_name, last_name, year, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.gpa = gpa

    def get_info(self):
        return f"{self.first_name} {self.last_name}, Year: {self.year}, GPA: {self.gpa}"







class PupilManager:
    def __init__(self):
        self.pupils=[]

    def add_pupil(self, pupil):
        self.pupils.append(pupil)


