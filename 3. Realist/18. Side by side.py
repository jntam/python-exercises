import textwrap


def sidebyside(left_str: str, right_str: str, width=79):
    if width % 2 == 1:
        side_width = width // 2
        # print(side_width)
    else:
        side_width = width // 2 - 1
        print(side_width)
    left_content = textwrap.wrap(left_str, width=side_width)
    right_content = textwrap.wrap(right_str, width=side_width)
    line_num = max(len(left_content), len(right_content))
    print("line:", line_num)
    left_content.extend([" " for index in range(line_num - len(left_content))])
    right_content.extend([" " for index in range(line_num - len(right_content))])
    print(left_content, "\n", right_content)
    result: str = ""
    for line in range(max(len(left_content), len(right_content))):
        result += left_content[line].ljust(side_width) + "|" + \
                  right_content[line].ljust(side_width) + "\n"
    return result


if __name__ == "__main__":
    left = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed non risus. "
        "Suspendisse lectus tortor, dignissim sit amet, "
        "adipiscing nec, utilisez sed sin dolor."
    )
    right = (
        "Morbi venenatis, felis nec pretium euismod, "
        "est mauris finibus risus, consectetur laoreet "
        "sem enim sed arcu. Maecenas sit amet eleifend sem. "
        "Nullam ac libero metus. Praesent ac finibus nulla, vitae molestie dolor."
        " Aliquam vestibulum viverra nisl, id porta mi viverra hendrerit."
        " Ut et porta augue, et convallis ante."
    )
    print(sidebyside('Hello world!', '42', width=10))
