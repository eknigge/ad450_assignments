# Percent to GPA
This program calculates the GPA based on an input percentage value. The percentage value can be an integer or floating point number. The program includes a test program `percent_gpa_test.py` which is used to validate the results and check for errors if the code is modified. 

# Running the Program
The program can be run or incorporated in several ways. One way is to import it into another program and use it to calculate GPA values. 

```
from percent_gpa import calculate_gpa 

print(calculate_gpa(95), calculate_gpa(84.2))
```

Another way to use it is from the command line and enter the percentage as a command line argument
```
python percent_gpa.py 95
```
This will print the result `4.0`. 
