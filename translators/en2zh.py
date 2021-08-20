# -*- coding: utf-8 -*-

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

modelUsing = "Helsinki-NLP/opus-mt-en-zh"

tokenizer = AutoTokenizer.from_pretrained(modelUsing)
model = AutoModelForSeq2SeqLM.from_pretrained(modelUsing)


def translate_en_zh(text):
    # Tokenize
    batch = tokenizer([text], return_tensors="pt", padding=True)

    # Perform the translation and decode the output
    translation = model.generate(**batch)
    result = tokenizer.batch_decode(translation, skip_special_tokens=True)

    return result[0]


if __name__ == "__main__":
    ans = translate_en_zh("Since employment is really like The end, I might really cry to Mr. Nachika")
    print(ans)
