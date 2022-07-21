def draw_n_squares(n):
    result: str = ""
    for i in range(n):
        top = "+---" * n + "+\n"
        middle = "|   "*n + "|\n"
        result += top + middle
    # print(top)
    bottom = "+---" * n + "+"
    result += bottom
    return result


if __name__ == "__main__":
    print(draw_n_squares(1))
