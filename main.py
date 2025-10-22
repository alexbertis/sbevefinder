
# Find and return the sbeve with parentheses
def find(text: str, subtext: str):
    working_subtext = subtext.lower()
    working_text = text.lower()
    text_index = 0
    result_text = ""
    for subindex, char in enumerate(working_subtext):
        found = False
        for index, t_char in enumerate(working_text[text_index:]):
            if char == t_char:
                found = True
                new_char = char if char == ' ' else f"({subtext[subindex]})"
                result_text += new_char
                text_index += index+1
                break
            else:
                result_text += text[index+text_index]
        if not found:
            return False, ""
    return True, result_text


if __name__ == '__main__':
    text = input('Enter the text where you want to find the sub-text:\n')
    subtext = input('Enter the sub-text to find:\n')
    success, result = find(text, subtext)
    if success:
        print("Sbeve! Found a match:")
        print(result)
    else:
        print("No match could be found :(")
