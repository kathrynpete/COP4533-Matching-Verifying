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
        self.match = -1
    def setFree(self):
        self.free = True
    def setMatched(self, match):
        self.match = match
        self.beenMatched.append(match)


def main(filename="./data/example.in"):
    #Read in data from example.in
    hospital_pref = []
    student_pref = []
    assignments = []
    n = 0 #setting a default value that will change
    #open file and automatically close after reading
    with open(filename, "r") as file:
        iterations = 0
        for line in file:
            #adding to list and converting to object
            if iterations == 0:
                #verify that n exists and can be converted to an integer
                try:
                    n = int(line.strip()) #storing n value
                except ValueError:
                    print("Error: Input file formatted incorrectly. There are no hospitals and students to match")
                    return hospital_pref, student_pref, assignments
            elif iterations <= n:
                hospital_pref.append(Candidate(id=int(iterations), pref_list=[int(num) for num in line.strip().split()]))
            elif iterations > n and iterations <= 2*n:
                 student_pref.append(Candidate(id=int(iterations-n), pref_list=[int(num) for num in line.strip().split()]))
            iterations += 1

    #verifying that there are the same number of hospitals and students
    if len(hospital_pref) != n or len(hospital_pref) != len(student_pref) or len(student_pref) != n:
        print("Error: There is not the same number of hospitals and students.")
        return hospital_pref, student_pref, assignments
    if len(hospital_pref)==0 or len(student_pref) == 0:
        print("Error: No students or hospitals available to match!")
        return hospital_pref, student_pref, assignments

    #Gale Shapley Algorithm
    #initialize lists
    free_hospitals = hospital_pref
    while len(free_hospitals) > 0:
        #Select a free hospital
        if free_hospitals[0].free == True:
            current_hospital = free_hospitals[0]
            for i in range(n):
                #select current hospital's top student
                top_student = current_hospital.pref_list[i]
                #if hospital and student have already been matched before, move on
                if top_student in current_hospital.beenMatched:
                    continue
                current_student = student_pref[top_student-1]
                if current_student.free == True:
                #assign student to hospital
                    #update students and hospitals assignment status
                    current_student.setTaken()
                    current_hospital.setTaken()
                    current_student.setMatched(current_hospital.id)
                    current_hospital.setMatched(current_student.id)
                    break
                else:
                    #student is not free
                    #check if student wants to trade up
                    student_trading_up = False
                    for j in range(n):
                        if current_student.pref_list[j] == current_student.match:
                            break #student likes current match better
                            
                        elif current_student.pref_list[j] == current_hospital.id:
                            #student decides to trade-up
                            student_trading_up = True
                            current_match = hospital_pref[(current_student.match)-1]
                            #add current match back to free list
                            free_hospitals.append(current_match)
                            #set current match as free hospital
                            current_match.setFree()
                            #match
                            current_hospital.setTaken()
                            current_hospital.setMatched(current_student.id)
                            current_student.setMatched(current_hospital.id)
                            break
                if student_trading_up:
                    break
        #decrease list of free hospitals to eventually break the while loop
        free_hospitals = free_hospitals[1:]
    #assign
    for pair in range(n):
        assignments.append((hospital_pref[pair].id, hospital_pref[pair].match))

    #write data to new file
    with open("./data/example.out", "w") as f:
        for (h, s) in assignments:
            f.write(f"{h} {s}\n")

    return hospital_pref, student_pref, assignments

if __name__ =="__main__":
  main()