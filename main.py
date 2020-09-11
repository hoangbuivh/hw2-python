#Author Hoang Bui hhb5051@psu.edu
def getGradeScore(grade): 
  if grade == "A": 
    return 4.0
  elif grade == "A-": 
    return 3.67
  elif grade == "B+": 
    return 3.33
  elif grade == "B": 
    return 3.0
  elif grade == "B-": 
    return 2.67
  elif grade == "C+": 
    return 2.33
  elif grade == "C": 
    return 2.0
  elif grade == "D": 
    return 1.0
  else: 
    return 0.0

def run():
  letterGrade1 = input("Enter your course 1 letter grade: ")
  credit1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradeScore(letterGrade1)}")

  letterGrade2 = input("Enter your course 2 letter grade: ")
  credit2 = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {getGradeScore(letterGrade2)}")

  letterGrade3 = input("Enter your course 3 letter grade: ")
  credit3 = float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {getGradeScore(letterGrade3)}")

  gpa = (getGradeScore(letterGrade1)*credit1 + getGradeScore(letterGrade2)*credit2 + getGradeScore(letterGrade3)*credit3)/(credit1+credit2+credit3)
  print(f"Your GPA is: {gpa}")
  
if __name__ == "__main__": 
  run()


