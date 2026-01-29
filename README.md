# COP4533-Matching-Verifying

Students: Maggie Yan (30309678), Kathryn Peters ()

1. Instructions to run the matcher:
    - located in ./src/matching_algo.py
    - main() default takes in "./data/example.in" file
    - to test different inputs, edit the ./data/example.in file with the input style specified in the assignment
    - the output will be written to ./data/example.out with the output style specified in the assignment

2. Instructions to run the verifier:
    - located in ./src/verifier.py
    - the verifier runs the algorithm once, before verifying the output
    - to match and verify the outputs of different inputs, edit the ./data/example.in file with the input style specified in the assignment
    - to run the verifier, use the default play button located in the upper right hand corner in vscode

3. Graph and solution to Task C:
    - The general trend we noticed when testing the run time of increasingly large inputs is that it takes an increasingly longer time, for both the matcher and the verifier. There is a little oscillation at the beginning of the matcher time complexity (e.g. 8 inputs takes slightly less time than 2 inputs; and 2^7 inputs takes slightly less timethan 2^6 inputs), but as n approaches larger and larger values (such as 2^9), the graph becomes exponential.
![alt text](./task_c_graphs/image.png)
![alt text](./task_c_graphs/image-1.png)

4. Extra notes:
    - if you want to run the time complexity file located in ./src/scalability.py, you must install matplotlib library to view the graphs
    - the folder ./testdata contains example inputs for testing the time complexity of the matcher and the verifier
