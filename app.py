def add(a, b):
    return a + b


def get_status():
    return "Jenkins pipeline is running!"


if __name__ == "__main__":
    print(get_status())
    print("2 + 3 =", add(2, 3))