from datetime import datetime
from typing import List

from dataclasses import dataclass


@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"


fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")


def separate_lines(te: str):
    lines_list: List[List[str]] = [[]]
    n: int = 0
    for sign in te:
        if sign == "\n":
            lines_list.append([])
            n += 1
        elif sign == te[-1]:
            lines_list[n].append(sign)
        else:
            lines_list[n].append(sign)
    lines = ["".join(x) for x in lines_list]
    # print(lines)
    line_length = [len(x) for x in lines]
    # print(line_length)
    return lines, line_length


def frame_text(te: str, frame: Frame) -> str:
    lines, lengths = separate_lines(te)
    max_length = max(lengths)
    lines_sta = "\n".join(y for y in [x.ljust(max_length) for x in lines])
    # print(lines_sta)
    lines_sta = lines_sta.replace("\n", "{}{}{}".format(frame.right, "\n", frame.left))
    # print(te)

    middle = "{}{}{}\n".format(frame.left, lines_sta, frame.right)
    top = frame.top_left + 1 * frame.top * max_length + frame.top_right + "\n"
    bottom = frame.bottom_left + 1 * frame.bottom * max_length + frame.bottom_right

    result = top + middle + bottom
    return result


if __name__ == "__main__":
    text = f"It \nis {datetime.now():%H:%I:%S}."
    text = frame_text(text, invisible_frame)
    text = frame_text(text, fancy_frame)
    text = frame_text(text, fancy_frame)
    print(text)
