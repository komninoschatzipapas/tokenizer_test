# Tokenizer Test

```
Regular:        ['▁test', '<unk>', '▁This', '▁is', '▁a', '▁test', '▁phrase', '</s>']
                <s> test<unk> This is a test phrase</s>
Legacy:         ['▁test', '<unk>', '▁', '▁This', '▁is', '▁a', '▁test', '▁phrase', '</s>']
                <s> test<unk>  This is a test phrase</s>
Fast:           ['▁test', '<unk>', '▁', '▁This', '▁is', '▁a', '▁test', '▁phrase', '</s>']
                <s> test<unk>  This is a test phrase</s>
Legacy Fast:    ['▁test', '<unk>', '▁', '▁This', '▁is', '▁a', '▁test', '▁phrase', '</s>']
```