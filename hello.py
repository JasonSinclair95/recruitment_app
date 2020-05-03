# Grade calcualtor
print("welcome to grade calculator")
maths_mark = int(input('please enter your maths marks: '))
chemistry_mark = int(input('please enter your chemistry marks: '))
physics_mark = int(input('please enter your physics marks: '))

total_marks = (maths_mark + chemistry_mark + physics_mark)

percentage_score = total_marks/3
print('your percentage score is: ', percentage_score,'%')

if percentage_score >= 70: 
    print("you scored a grade of A")
elif percentage_score >= 60: 
    print("you scored a grade of B")
elif percentage_score >= 50: 
    print("you scored a grade of C")
elif percentage_score >= 40: 
    print("you scored a grade of D")
elif percentage_score < 40: 
    print("you failed")
else:
    print('enter marks again')


