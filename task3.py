import pandas as pd
import datetime as dt
import pytz

def data_prepare():

    lessons = pd.read_csv('tech_quality/lessons.txt', sep="|", header=None, names=["lesson_id", "event_id", "subject", "scheduled_time"])
    participants = pd.read_csv('tech_quality/participants.txt', sep="|", header=None, names=["event_id", "user_id"])
    quality = pd.read_csv('tech_quality/quality.txt', sep="|", header=None, names=["lesson_id", "tech_quality"])
    users = pd.read_csv('tech_quality/users.txt', sep="|", header=None, names=["user_id", "role"])

    data = []

    lessons = lessons[lessons.subject == "phys"]
    sub = lessons.merge(participants, 'left', on='event_id')
    sub = sub.merge(users, 'left', on='user_id')
    sub = sub[sub.role == "tutor"]
    sub = sub.drop_duplicates(subset='event_id', keep="first")

    for index, row in sub.iterrows():
        lesson_mark = quality[quality.lesson_id == row.lesson_id]
        lesson_mark = lesson_mark.fillna(0)
        temp = 0

        casual_time = pytz.utc.localize(dt.datetime.fromisoformat(row.scheduled_time)).astimezone(pytz.timezone('Europe/Moscow'))
        casual_time = casual_time.strftime("%Y-%m-%d")

        if lesson_mark.empty:
            continue
        else:
            i = 0
            for index1, row1 in lesson_mark.iterrows():
                temp += row1.tech_quality
                i += 1

        if temp == 0:
            continue

        if len(data) == 0:
            data.append([casual_time,
                         row.user_id,
                         temp, i])
            continue

        for j in range(len(data)):
            if row.user_id in data[j] and casual_time in data[j]:
                data[j][2] += temp
                data[j][3] += i
                break
            elif j == (len(data) - 1):
                data.append([casual_time,
                         row.user_id,
                         temp, i])

    return data

def post_data_analize(data):

    result = []

    for i in range(len(data)):
        middle_mark = round(data[i][2] / data[i][3], 2)

        if len(result) == 0:
            result.append([data[i][0], data[i][1], middle_mark])
        else:
            for j in range(len(result)):
                if data[i][0] in result[j]:
                    if middle_mark < result[j][2]:
                        result[j][1] = data[i][1]
                        result[j][2] = middle_mark
                    break
                elif j == len(result) - 1:
                    result.append([data[i][0], data[i][1], middle_mark])

    for i in result:
        print(i, "\n")

if __name__ == '__main__':
    data = data_prepare()
    post_data_analize(data)

