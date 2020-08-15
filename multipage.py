import re


def squash(text: str):
    return "".join(text.split())


def sparse_substrings(text: str):
    """puts spaces between numbers and the rest of text elements elements"""
    groups = re.findall(r"\D{1,}", text)

    out = text
    # print(f"{out} - Cleanup starting...")
    for substring in groups:
        sparsed = f" {squash(substring)} "
        out = out.replace(substring, sparsed)
        # print(f"{out} - (Found r: '{result}' -> '{sparsed}')")

    # print(f"{out} - after sparse ")
    return out


def collapse_numbers(text: str):
    """handles spaced digits as part of the same number"""
    groups = re.findall(r"[\d|\s]{1,}", text)

    results = list()
    for numbers in groups:
        squashed = squash(numbers)
        if squashed != "":
            results.append(squashed)

    return results


def extract_numbers(text: str):
    sparsed_text = sparse_substrings(text)
    numbers = collapse_numbers(sparsed_text)
    return [int(number) for number in numbers]


if __name__ == "__main__":

    ocr_samples = [
        "8/10", "2 of10", " 3", "page 31 2", "9- 1 0", "page 2-   4s", "2-3",
        "2. 10"
    ]

    for t in ocr_samples:
        n = extract_numbers(t)
        print(f"{t} -> {n}")


# Known cases
# -----------
# extracted from text (e.x. 1 / 20)
# extracted from text (e.x: 1)
# extracted from text (e.x. 1 / 20) + element for identification
# consecutive means same
# consecutive means same + element for identification
