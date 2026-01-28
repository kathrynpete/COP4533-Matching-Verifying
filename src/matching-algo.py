
#object to define hospitals and students 
class Candidate:
    def __init__(self, id, pref_list):
        self.free = True
        self.id = id
        self.pref_list = pref_list
        self.match = -1
    def setTaken(self):
        self.free = False
    def setMatch(self, match):
        self.match = match

def main():
    #Read in data from example.in
    hospital_pref = []
    student_pref = []
    n = 0 #setting a default value that will change
    #open file and automatically close after reading
    with open("./data/example.in", "r") as file:
        iterations = 0
        index = 0
        for line in file:
            #adding to list and converting to object
            if iterations == 0:
                #verify that n exists and can be converted to an integer
                try:
                    n = int(line.strip()) #storing n value
                except ValueError:
                    print("There are no hospitals and students to match")
                    return
            elif iterations <= n:
                hospital_pref.append(Candidate(id=iterations, pref_list=[int(num) for num in line.strip() if num != " "]))
            elif iterations > n and iterations <= 2*n:
                 student_pref.append(Candidate(id=iterations-n, pref_list=[int(num) for num in line.strip() if num != " "]))
                # student_pref.append([Candidate(id=num) for num in line.strip() if num!= " "])
            iterations += 1
            
    #testing
    # for i in range(n):
    #     print(f"{hospital_pref[i].id}")
    #     print(f"{hospital_pref[i].pref_list}") #testing
    #     print(f"{student_pref[i].id}")
    #     print(f"{student_pref[i].pref_list}") #testing
        
        # print(f"{student_pref[i][0].id}, {student_pref[i][1].id}, {student_pref[i][2].id}") #testing

    #verifying that there are the same number of hospitals and students
    if len(hospital_pref) != n or len(hospital_pref) != len(student_pref) or len(student_pref) != n:
        print("Error: There is not the same number of hospitals and students.")
        return
    if len(hospital_pref)==0 or len(student_pref) == 0:
        print("Error: No students or hospitals available to match!")
    
    #testing
    # print(n)
    # print(hospital_pref)
    # print(student_pref)

    #Gale Shapley Algorithm
    # free_hospitals = n
    index = 1
    free_hospitals = hospital_pref
    assignments = []
    while len(free_hospitals) != 0:
       #Select a free hospital
        if free_hospitals[0].free == True:
            free_hospital = free_hospitals[0]
            for i in range(n):
                top_student = free_hospital.pref_list[i]
                # print("top student: ", top_student)
                if student_pref[top_student-1].free == True:
                #assign student to hospital
                    assignments.append((free_hospital.id, student_pref[top_student-1].id))
                    #update students and hospitals free status
                    student_pref[top_student-1].setTaken()
                    free_hospital.setTaken()
                    student_pref[top_student-1].setMatch(free_hospital.id)
                    free_hospital.setMatch(student_pref[top_student-1].id)
                    free_hospitals = free_hospitals[1:]
                    print("first condition")
                    break
                else:
                    print("student not free")
                    #student is not free
                    #check if student wants to trade up
                    for j in range(n):
                        if student_pref[top_student-1].pref_list[j] == student_pref[top_student-1].match:
                            print("student not trading up")
                            break #student likes current match better
                            
                        elif student_pref[top_student-1].pref_list[j] == free_hospital.id:
                            free_hospitals.append((hospital_pref[student_pref[top_student-1].match])-1)
                            free_hospital.setTaken()
                            student_pref[top_student-1].setMatch(free_hospital.id)
                            free_hospital.setMatch(student_pref[top_student-1].id)
                            free_hospitals = free_hospitals[1:]
                            print("student traded up")

    
        # free_hospitals = hospital_pref[1:]
        index += 1
    print(assignments)

if __name__ =="__main__":
  main()