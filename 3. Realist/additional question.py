from dataclasses import dataclass
from datetime import datetime
from typing import List


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

    def draw_top_line(self, content_width: int):
        top = self.top_left + 1 * self.top * content_width + self.top_right + "\n"
        return top

    def draw_body_line(self, single_line_content: str, content_width: int):
        lines_list, _ = separate_lines(single_line_content)
        lines_sta = "\n".join(y for y in [x.ljust(content_width) for x in lines_list])
        lines_sta = lines_sta.replace("\n", "{}{}{}".format(self.right, "\n", self.left))
        middle = "{}{}{}\n".format(self.left, lines_sta, self.right)
        return middle

    def draw_bottom_line(self, content_width: int):
        bottom = self.bottom_left + 1 * self.bottom * content_width + self.bottom_right
        return bottom

    def draw_content(self, content_width: int):
        full_content = Frame.draw_top_line(self, content_width) + \
                       Frame.draw_body_line(self, "", content_width) + \
                       Frame.draw_bottom_line(self, content_width)
        return full_content


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
    # text = frame_text(text, invisible_frame)
    # text = frame_text(text, fancy_frame)
    # text = frame_text(text, fancy_frame)
    print(text)
    print(Frame.draw_top_line(fancy_frame, 13), "\n")
    print(Frame.draw_body_line(fancy_frame, text, 13), "\n")
    print(Frame.draw_bottom_line(fancy_frame, 13), "\n")
    print(Frame.draw_content(fancy_frame, 13), "\n")
