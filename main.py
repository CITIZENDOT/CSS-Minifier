from math import log, ceil
import itertools
from string import ascii_lowercase
from utils import class_patterns, id_patterns


def get_small_selectors(selectors):
    n = len(selectors)
    if n == 0:
        return {}
    max_chars_in_selector = max(ceil(log(n, 26)), 1)
    short_selectors = []
    for i in range(1, max_chars_in_selector + 1):
        tmp = ["".join(i) for i in itertools.product(ascii_lowercase, repeat=i)]
        short_selectors.extend(tmp)
    short_selectors = short_selectors[:n]

    cls_map = {}
    for i, selector in enumerate(selectors):
        cls_map[selector] = short_selectors[i]

    return cls_map


def get_selectors(html_string, patterns):
    selectors = []
    for pattern in patterns:
        selectors.extend(pattern.findall(html_string))

    for i, selector in enumerate(selectors):
        selectors[i] = selector[1]
    return selectors


def get_frequency_map(selectors):
    frq = {}
    for cls in selectors:
        if cls not in frq:
            frq[cls] = 0
        frq[cls] += 1
    return frq


def replace_class(cls_map, match):
    prefix = match.group(1)
    cls = match.group(2).split(" ")
    suffix = match.group(3)
    return prefix + " ".join(cls_map[i] for i in cls) + suffix


def get_final_source(class_map, id_map, html_string):
    for pattern in class_patterns:
        html_string = pattern.sub(lambda x: replace_class(class_map, x), html_string)
    for pattern in id_patterns:
        html_string = pattern.sub(lambda x: replace_class(id_map, x), html_string)
    return html_string


def get_selector_map(html_string, patterns):
    selectors = get_selectors(html_string, patterns)
    if len(selectors) == 0:
        return {}
    selector_frq = get_frequency_map(selectors)

    all_selectors = list(selector_frq.keys())
    all_selectors.sort(key=lambda cls: selector_frq[cls], reverse=True)
    selector_map = get_small_selectors(all_selectors)
    return selector_map


def main():
    with open("source.html", "r") as f:
        html_string = f.read()

    class_map = get_selector_map(html_string, class_patterns)
    id_map = get_selector_map(html_string, id_patterns)

    short_source = get_final_source(class_map, id_map, html_string)
    with open("optimized_source.html", "w") as f:
        f.write(short_source)


if __name__ == "__main__":
    main()
