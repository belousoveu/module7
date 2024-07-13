team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / tasks_total

print('В команде %s участников: %d!' % (team1, team1_num))
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))
print("Команда {0} решила задач: {1}".format(score2, team2))
print(" Волшебники данных решили задачи за {} с !".format(team2_time))
print(f'Команды решили {score1} и {score2} задач.')
if score1 > score2 or (score1 == score2 and team2_time > team1_time):
    winner = team1
else:
    winner = team2
print(f'Результат битвы: победа команды {winner}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!.')