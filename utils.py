import requests
from datetime import datetime


def get_data(url):
    try:
        responce = requests.request("GET", url, verify=False)
        if responce.status_code == 200:
            return responce.json(), "INFO: Данные получены успешно\n"
        return None, f"ERROR status_code:{responce.status_code}\n"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError\n"
    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError"


def get_filtred_data(data, filtered_empty_from=False):
    # pprint(data[:5])
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    formatted_data = []
    for row in data:
        data = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]
        from_info, from_bill = "", ""
        if "from" in row:
            sender = row["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = " ".join(sender)
        to = f"{row['to'].split()[0]} **{row['to'][-4:]}"
        operation_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        formatted_data.append(f"""\
{data} {description}
{from_info} {from_bill} -> {to}
{operation_amount}""")
    return formatted_data
