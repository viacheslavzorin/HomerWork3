from utils import get_data


def main():
    URL = "https://jsonkeeper.com/b/Y2L2"
    data, info = get_data(URL)
    if not data:
        exit(info)
    else:
        print(info)


if __name__ == "__main__":
    main()
