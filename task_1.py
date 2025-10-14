count_time = 0
time = '1h 45m,360s,25m,30m 120s,2h 60s'
lst = time.replace(' ',',')
total_time = lst.split(',')

for i in total_time:
    if 'h' in i:
        count_time += int(i[:-1])*60
    if 'm' in i:
        count_time += int(i[:-1])
    if 's' in i:
        count_time += int(i[:-1])//60
print(count_time)