import re

def convert_hashtags(text):
    return re.sub(r'#(\w+)', r'<a href="\1">#\1</a>', text)

text = "Erico #tag"
converted_text = convert_hashtags(text)
print(converted_text)