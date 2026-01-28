
#object to define hospitals and students 
class Candidate:
    def __init__(self, id, pref_list):
        self.free = True
        self.id = id
        self.pref_list = pref_list
        self.match = -1
        self.beenMatched = []
    def setTaken(self):
        self.free = False
    def setFree(self):
        self.free = True
    def setMatched(self, match):
        self.match = match
        self.beenMatched.append(match)


def main():
    #Read in data from example.in
    hospital_pref = []
    student_pref = []
    n = 0 #setting a default value that will change
    #open file and automatically close after reading
    #verify file opening works
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
    #initialize lists
    free_hospitals = hospital_pref
    assignments = []
    while len(free_hospitals) > 0:
        #Select a free hospital
        if free_hospitals[0].free == True:
            current_hospital = free_hospitals[0]
            #testing
            print(f"current hospital {current_hospital.id}")
            for i in range(n):
                top_student = current_hospital.pref_list[i]
                #if hospital and student have already been matched before, move on
                if top_student in current_hospital.beenMatched:
                    #testing
                    print(f'already been matched iteration is now {i}')
                    continue
                current_student = student_pref[top_student-1]
                if current_student.free == True:
                #assign student to hospital
                    #update students and hospitals free status
                    current_student.setTaken()
                    current_hospital.setTaken()
                    current_student.setMatched(current_hospital.id)
                    current_hospital.setMatched(current_student.id)
                    #testing
                    print("first condition")
                    break
                else:
                    print("student not free")
                    #student is not free
                    #check if student wants to trade up
                    for j in range(n):
                        if current_student.pref_list[j] == current_student.match:
                            #testing
                            print("student not trading up")
                            break #student likes current match better
                            
                        elif student_pref[top_student-1].pref_list[j] == current_hospital.id:
                            #student decides to trade-up
                            current_match = hospital_pref[(current_student.match)-1]
                            #add current match back to free list
                            free_hospitals.append(current_match)
                            #set current match as free hospital
                            current_match.setFree()
                            #match
                            current_hospital.setTaken()
                            current_hospital.setMatched(current_student.id)
                            current_student.setMatched(current_hospital.id)
                            #testing
                            print("student traded up")
                            break
                break
        free_hospitals = free_hospitals[1:]

    #assign
    for pair in range(n):
        assignments.append((hospital_pref[pair].id, hospital_pref[pair].match))
    #testing
    print(assignments)
    return assignments

if __name__ =="__main__":
  main()