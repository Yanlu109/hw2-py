#Author: Yan Lu yfl5541@psu.edu
def getGradePoint(grade1):
  if grade1 == "A":
    gp1 = 4.0
  elif grade1 == "A-":
    gp1 = 3.67
  elif grade1 == "B+":
    gp1 = 3.33
  elif grade1 == "B":
    gp1 = 3.0
  elif grade1 == "B-":
    gp1 = 2.67
  elif grade1 == "C+":
    gp1 = 2.33
  elif grade1 == "C":
    gp1 = 2.0
  elif grade1 == "D":
    gp1 = 1.0
  else:
    gp1 = 0.0
  return gp1
def getGradePiont(grade2):
  if grade2 == "A":
    gp2 = 4.0
  elif grade2 == "A-":
    gp2 = 3.67
  elif grade2 == "B+":
    gp2 = 3.33
  elif grade2 == "B":
    gp2 = 3.0
  elif grade2 == "B-":
    gp2 = 2.67
  elif grade2 == "C+":
    gp2 = 2.33
  elif grade2 == "C":
    gp2 = 2.0
  elif grade2 == "D":
    gp2 = 1.0
  else:
    gp2 = 0.0
  return gp2
def getGradePiont(grade3):
  if grade3 == "A":
    gp3 = 4.0
  elif grade3 == "A-":
    gp3 = 3.67
  elif grade3 == "B+":
    gp3 = 3.33
  elif grade3 == "B":
    gp3 = 3.0
  elif grade3 == "B-":
    gp3 = 2.67
  elif grade3 == "C+":
    gp3 = 2.33
  elif grade3 == "C":
    gp3 = 2.0
  elif grade3 == "D":
    gp3 = 1.0
  else:
    gp3 = 0.0
  return gp3

def run():
  grade1 = input("Enter your course 1 letter grade: ")
  credit1 = input("Enter your course 1 credit: ")
  print(f"Grade point for course 1 is: {getGradePoint(grade1)}")
  grade2 = input("Enter your course 2 letter grade: ")
  credit2 = input("Enter your course 2 credit: ")
  print(f"Grade point for course 2 is: {getGradePoint(grade2)}")
  grade3 = input("Enter your course 3 letter grade: ")
  credit3 = input("Enter your course 3 credit: ")
  print(f"Grade point for course 3 is: {getGradePoint(grade3)}")

  gpa = float((int(credit1)* getGradePoint(grade1) + int(credit2) * getGradePoint(grade2) + int(credit3) * getGradePoint(grade3))/(int(credit1) + int(credit2) + int(credit3)))

  print(f"Your GPA is: {gpa}")
  

if __name__=="__main__":
  run()

 