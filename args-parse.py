import argparse

parser = argparse.ArgumentParser(description="""
create student profiles
""")

parser.add_argument("fname", help="First name of the student")
parser.add_argument("lname", help="Last name of the student")
parser.add_argument("--mname", help="Middle name of the student")
parser.add_argument("gender", choices=["m","f"],help="Gender of student m/f")
parser.add_argument("--age", default=18)

args = parser.parse_args()

fname = args.fname
lname = args.lname
mname = args.mname
gender = args.gender
age = str(args.age)

if mname is None:
    print("Name: " + fname + " " + lname)
else:
    print("Name: " + fname + " " + mname + " " + lname)    
print("age: " + age)
print("Gender: " + gender)
print("Finish")