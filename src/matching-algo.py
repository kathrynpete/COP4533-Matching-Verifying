
#object to define hospitals and students 
class Candidate:
    def __init__(self, id):
        self.free = True
        self.id = id
    def setTaken(self):
        self.free = False

def main():
    #Read in data from example.in
    hospital_pref = []
    student_pref = []
    n = 0 #setting a default value that will change
    #open file and automatically close after reading
    with open("./data/example.in", "r") as file:
        iterations = 0
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
                hospital_pref.append([Candidate(id=num) for num in line.strip() if num!= " "])
            elif iterations > n and iterations <= 2*n:
                student_pref.append([Candidate(id=num) for num in line.strip() if num!= " "])
            iterations += 1
    #testing
    # for i in range(n):
    #     print(f"{hospital_pref[i][0].id}, {hospital_pref[i][1].id}, {hospital_pref[i][2].id}") #testing
    #     print(f"{student_pref[i][0].id}, {student_pref[i][1].id}, {student_pref[i][2].id}") #testing

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
    free_hospitals = n
    while free_hospitals > 0:
       #Select a free hospital
       break
    

if __name__ =="__main__":
  main()