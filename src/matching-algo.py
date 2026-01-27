def main():
    #Read in data from example.in
    pref_list = []
    #open file and automatically close after reading
    with open("../data/example.in", "r") as file:
        for line in file:
            #adding to list and converting to int
            pref_list.append([int(num) for num in line.strip() if num!= " "])
    print(pref_list) #testing

    n = pref_list[0][0] #number of hospitals and students
    hospital_pref = pref_list[1:n+1] #hospital preference lists
    student_pref = pref_list[n+1 : 2*n+1 ] #student preference lists
    if len(hospital_pref) != n != len(student_pref):
        print("Error: There is not the same number of hospitals and students.")
        return
    
    #testing
    # print(n)
    # print(hospital_pref)
    # print(student_pref)

    #Gale Shapley Algorithm
    free_hospitals = n
    while free_hospitals > 0:
       #Select a free hospital
       pass
    

if __name__ =="__main__":
  main()