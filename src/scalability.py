import os
from time import time
from matching_algo import main
from verifier import valid_matching, stable_matching
import matplotlib.pyplot as plt

n_size = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

os.makedirs("test_data", exist_ok=True)

algo_time = []
verify_time = []

'''
code for generating test files:

for n in n_size:
  filename = f"test_data/example_{n}.in"
  with open(filename, "w") as f:
    f.write(f"{n}\n")
    # hospital preferences (first n lines)
    for i in range(n):
      pref_list = [(i + j) % n + 1 for j in range(n)]
      f.write(" ".join(map(str, pref_list)) + "\n")
    # student preferences (next n lines)
    for i in range(n):
      pref_list = [(i + j) % n + 1 for j in range(n)]
      f.write(" ".join(map(str, pref_list)) + "\n")

'''

for n in n_size:
  filename = f"test_data/example_{n}.in"
  t0 = time()
  hospital_pref, student_pref, assignments = main(filename)
  t1 = time()
  algo_time.append(t1 - t0)

  t3 = time()
  valid_matching(assignments)
  stable_matching(hospital_pref, student_pref, assignments)
  t4 = time()
  verify_time.append(t4 - t3)

# figure 1: algorithm time and verification time side by side
fig = plt.figure(figsize =(10, 10))

sub1 = plt.subplot(1, 2, 1)
sub2 = plt.subplot(1, 2, 2)

sub1.plot(n_size, algo_time)

sub1.set_xticks(n_size)
sub1.set_title('Gale-Shapley Algorithm Time')
sub1.set_xlabel('Number of Hospitals/Students (n)')
sub1.set_ylabel('Time (seconds)')
sub1.set_xscale('log', base=2)

sub2.plot(n_size, verify_time)

sub2.set_xticks(n_size)
sub2.set_title('Verification Time')
sub2.set_xlabel('Number of Hospitals/Students (n)')
sub2.set_ylabel('Time (seconds)')
sub2.set_xscale('log', base=2)

# figure 2: algorithm time and verification time on same plot
fig2 = plt.figure(figsize=(10, 6))

plt.plot(n_size, algo_time, marker='o', label='Gale-Shapley Algorithm')
plt.plot(n_size, verify_time, marker='o', label='Verifier')

plt.xticks(n_size)
plt.title('Running Time vs n')
plt.xlabel('Number of Hospitals/Students (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.xscale('log', base=2)
plt.tight_layout()
plt.show()

print(algo_time)
print(verify_time)