emojis = {
"happy": "😃",
"heart": "😍",
"rotfl": "🤣",
"smile": "😊",
"crying": "😭",
"kiss": "😘",
"clap": "👏",
"grin": "😁",
"fire": "🔥",
"broken": "💔",
"think": "🤔",
"excited": "🤩",
"boring": "🙄",
"winking": "😉",
"ok": "👌",
"hug": "🤗",
"cool": "😎",
"angry": "😠",
"python": "🐍"
}

sentence = input("Please enter a sentence: ")

words = sentence\
            .replace('!', ' ')\
            .replace('.', ' ')\
            .replace(',', ' ')\
            .split()

translated = [(emojis[f'{x.lower()}']) if x.lower() in emojis.keys() else x for x in words]

new_sentence = ' '
new_sentence = new_sentence.join(translated)

print(new_sentence)