questions = ['What is capital of India?','What is capital of Germany?','What is capital of UAE?']
options = [['Mumbai','Kolkata','Pune','New Delhi'],['Berlin','Munich','Hamburg','Frankfurt'],['Dubai','Cairo','Nairobi','Abu Dhabi']]
correct_answers = [4,1,4]
prize_money = [10000,20000,30000]
total_money = 0


for i in range(len(questions)):
    print(questions[i])
    print('Your options are : ')
    for j in range(len(options)+1):
        print(f'{j+1}.',options[i][j])
    user_input = int(input('Enter your answer: '))
    if user_input == correct_answers[i]:
        total_money += prize_money[i]
    else:
        print('You Lost!')
        break

print('You won - rs', total_money)