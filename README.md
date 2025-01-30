# neo-lang
Proof of concept of using LLMs to make conlangs

## How does it work
This project shows that, while LLMs are not good enough to make fully fledged constructed languages, pairing their generative abilities with symbolic calculation is enough to make interesting experiments.
In this case, the LLM is required to generate a YAML file which contains
1. A list of word roles and corresponding morphosyntaxic regex
2. A context-free grammar to manage sentence creation and word order
3. A list of transliteration rules to convert the sentences to IPA

The prompt can be found here.
You should then talk with the agent to ask it to change the grammar the alphabet or anything about the language.
You can use the transliteration for converting to other alphabets to :)

Feel free to share your language creations !

## Contributing
This is a fun one day experiment project and it's thus quite a bit limited.

Here are some possible improvements:
- Improve the prompt
- Use grammars intead of regular languages for word roles, for example detail vowel consonants patterns such as CVCV
- Use context-dependent grammars for sentence creation
- Use a finite-state transductor for transliteration
- Implement word inflexion (conjugation, case, number, gender, etc.)

If you want to improve the project, feel free to PR.
