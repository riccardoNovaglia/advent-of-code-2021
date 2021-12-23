def get_cleaned_up_input() -> [str]:
    with open("./input.txt", "r") as file:
        contents = file.read()
    return list(filter(lambda line: line != "", contents.split("\n")))


def get_raw_input() -> [str]:
    with open("./input.txt", "r") as file:
        return file.read()
