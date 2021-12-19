from datetime import datetime

def get_time_difference(datetime_str, query_dt):
    dt = datetime.strptime(datetime_str, '%Y-%m-%d  %H:%M:%S')

    diff = dt - query_dt
    if (diff.seconds // 60) < 2:
        print('%s - %s\n' % (dt, query_dt))
    # print((diff.seconds // 60))
    return (diff.seconds // 60)