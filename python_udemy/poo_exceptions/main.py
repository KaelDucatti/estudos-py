class MyError(Exception):
    pass


def get_my_error():
    exception_ = MyError("a", "b", "c")
    raise exception_


def main():
    try:
        get_my_error()
    except MyError as error:
        print(error)


if __name__ == "__main__":
    main()
