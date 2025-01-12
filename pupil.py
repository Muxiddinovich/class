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
    

    def get_pupils(self):
        for pupil in self.pupils:
            print(pupil.get_info())



    def get_max_gpa(self):
        gpa=0
        for pupil in self.pupils:
            if pupil.gpa > gpa:
                gpa = pupil.gpa

        return gpa
    


    def change_gpa(self, ism, fam, new_gpa):
        for pupil in self.pupils:
            if pupil.ism==ism and pupil.fam==fam:
                pupil.gpa = new_gpa







pupil1=Pupil("Sherbek", "Kubayev", 2008, 100)
pupil2=Pupil("Sherbek2", "Kubayev2", 2008, 90)


manager=PupilManager()
manager2=PupilManager()

manager.add_pupil(pupil1)
manager.add_pupil(pupil2)

manager.change_gpa("Sherbek2", "Kubayev2", 110)






manager.get_pupils()



