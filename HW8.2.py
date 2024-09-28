import statistics

two_meters: int = 0
data: list[float] = []
avg: float = 0
while True:
    players: float = float(input('enter your high:'))
    if players == -999:
        break
    if players >= 3.0 or players <= 1.60:
        continue
    data.append(players)
    if players > 2.0:
        two_meters += 1
        data.append(players)
    if players == -999:
        break
print('How many players were taken in?', len(data))
print('The height of the tallest player:', max(data))
print('The height of the shortest player:', min(data))
print('Average height of the players:', statistics.mean(data))
print(f'Some players are taller than 2.0 meters:{two_meters}')
