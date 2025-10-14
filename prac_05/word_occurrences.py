"""
CP1404/CP5632 Practical05
Word Occurrences
Estimate: 20 minutes
Actual: 30 minutes (Made a coffee...)
"""

def main():
    """Count occurrences of words in a string"""
    dissected_text = {}
    text = input("Text: ")
    for word in text.split():
        if word in dissected_text:
            dissected_text[word] += 1
        else:
            dissected_text[word] = 1
    for word in sorted(dissected_text):
        print(f"{word:{10}} : {dissected_text[word]}")


main()