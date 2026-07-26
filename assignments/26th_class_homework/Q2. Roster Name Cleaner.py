def normalize_name(raw):
    parts = raw.strip().split()
    join=" ".join(words.title() for words in parts)
    return join


name=input()
normalize_name(name)