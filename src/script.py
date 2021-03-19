# -*- coding: utf-8 -*-
import pandas as pd
from distanceUtil import get_distance_matrix
from MetroGraph import Station, Line, MetroMap

next_id = 0
# id -> Station
stations = {}
lines = {}

data = pd.read_csv('../datasets/Beijing.csv')

line_names = list(set(list(data['公交名'])))
for name in line_names:
    loop = False
    if name == '北京地铁10号线':
        loop = True
    lines[name] = Line(name, loop)

for record in data.values:
    # record format:
    # 城市,公交名,首末班车时间,起始站,起始站经度,起始站纬度,终点站,终点站经度,终点站纬度,站点名,最高价,英文名,站数,经度,纬度,性质,线路ID,区号,区县编码,站点ID,总站数,发车间隔,线路总长度,基础价格,站点状态,ICCARD
    line = lines[record[1]]
    station_name = record[9]
    station_logitude = record[13]
    station_latitude = record[14]
    station = Station(station_name, station_logitude, station_latitude) 
    if station not in stations.values():
        stations[next_id] = station
        next_id += 1
    line.add_station(station)

beijingMetro = MetroMap(stations, lines)

#build edge_matrix
edge_matrix = beijingMetro.produce_matrix()

# distance_matrix[i][j]:
# shortest metro path from station i to station j
distance_matrix = get_distance_matrix(edge_matrix);

#absolote path
absolute_matrix = beijingMetro.produce_absolute_distance_matrix();

metro_sum = 0
absolute_sum = 0
for i in range(len(distance_matrix)):
    for j in range(len(distance_matrix)):
        metro_sum += distance_matrix[i][j]
        absolute_sum += absolute_matrix[i][j]

print("北京地铁平均地铁里程/绝对距离：")
print(metro_sum/absolute_sum)