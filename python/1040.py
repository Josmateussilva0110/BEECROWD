grade1, grade2, grade3, grade4 = input().split()
grade1 = float(grade1)
grade2 = float(grade2)
grade3 = float(grade3)
grade4 = float(grade4)
total = grade1* 2 + grade2 * 3 + grade3 * 4 + grade4 * 1
average = total / 10
print(f'Media: {average:.1f}')
if average >= 7.0:
    print('Aluno aprovado.')
elif average < 5.0:
    print('Aluno reprovado.')
elif average >= 5.0 and average <= 6.9:
    print('Aluno em exame.')
    grade5 = float(input())
    print(f'Nota do exame: {grade5:.1f}')
    tot = (grade5 + average) / 2
    if tot >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {tot:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {tot:.1f}')
