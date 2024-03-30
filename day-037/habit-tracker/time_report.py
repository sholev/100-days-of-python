import csv, json
from datetime import datetime


def get_report_data():
    data = {}
    with open("time-report.csv", "r") as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader):
            date = datetime.strptime(row["Start Date"], "%d/%m/%Y")
            key = date.strftime("%Y%m%d")

            if key in data:
                data[key]["quantity"] += float(row["Duration (decimal)"])
                opt_data = [{
                    "Start Time (%H:%M:%S)": row["Start Time"],
                    "Duration (%H:%M:%S)": row["Duration (h)"],
                }]
                opt_data.extend(json.loads(data[key]["optionalData"]))
                data[key]["optionalData"] = json.dumps(opt_data)
            else:
                data[key] = {
                    "quantity": float(row["Duration (decimal)"]),
                    "optionalData": json.dumps([{
                        "Start Time (%H:%M:%S)": row["Start Time"],
                        "Duration (%H:%M:%S)": row["Duration (h)"],
                    }])
                }
    return data


def print_report():
    data = get_report_data()
    for key in data:
        print(f"{key}:{data[key]}")


# print_report()
