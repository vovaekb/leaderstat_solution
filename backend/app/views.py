import json
import csv
from datetime import datetime
from flask import Flask, request, jsonify, Response
from app import app
from app.utils import get_time_difference


@app.route('/', methods=['GET'])
def index():
    return Response('Hello', status=200)


@app.route('/get_overload', methods=['POST'])
def get_overload():
    query_data = request.get_json()
    location = query_data['location'] # 'Автозаводский мост'
    print(location)
    query_datetime = datetime.strptime(query_data['time'], '%Y-%m-%d  %H:%M:%S') # '2021-12-21 14:35:36'
    print(query_data['time'])
    with open('app/out.csv') as f:
        reader = csv.DictReader(f)

        filtered_by_loc_records = list(filter(lambda x:
                                              x['Location'] == location,
                                              list(reader))
                                       )
        filtered_by_time_records = list(filter(lambda x:
                                          get_time_difference(
                                              x['DataTime'],
                                              query_datetime
                                          ) < 3,
                                          filtered_by_loc_records))
        target_record = filtered_by_time_records[0]
        print(len(filtered_by_time_records))

        overload_value = int(target_record['count_pass']) / int(target_record['Max_count'])
        overload_value *= 5
        overload_value = int(overload_value)
        print(f'{overload_value}')
        data = {
            "overload_value": overload_value
        }
    return jsonify(data)