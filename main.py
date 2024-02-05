from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('.', legacy=False, use_fast=False)
tokenizerl = AutoTokenizer.from_pretrained('.', legacy=True, use_fast=False)
tokenizerf = AutoTokenizer.from_pretrained('.', legacy=False, use_fast=True)
tokenizerlf = AutoTokenizer.from_pretrained('.', legacy=True, use_fast=True)

s = "test<unk> This is a test phrase</s>"

print(
  f'Regular:\t{tokenizer.tokenize(s)}\n\t\t{tokenizer.decode(tokenizer.encode(s))}'
)

print(
  f'Legacy:\t\t{tokenizerl.tokenize(s)}\n\t\t{tokenizerl.decode(tokenizerl.encode(s))}'
)

print(
  f'Fast:\t\t{tokenizerf.tokenize(s)}\n\t\t{tokenizerf.decode(tokenizerf.encode(s))}'
)

print(
  f'Legacy Fast:\t{tokenizerlf.tokenize(s)}\n\t\t{tokenizerlf.decode(tokenizerlf.encode(s))}'
)
