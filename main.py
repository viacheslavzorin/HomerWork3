from utils import get_data, get_filtred_data, get_last_values, get_formatted_data


def main():
    URL = "https://jsonkeeper.com/b/Y2L2"
    FILTERED_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5

    data, info = get_data(URL)
    if not data:
        exit(info)
    else:
        print(info)

    data = get_filtred_data(data, filtered_empty_from=FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    print(data)
    print("INFO: Вывод данных:\n")
    for row in data:
        print(row, end="\n\n")


if __name__ == "__main__":
    main()
