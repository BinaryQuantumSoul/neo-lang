# neo-lang
Proof of concept of using LLMs to make conlangs

![imagen](https://github.com/user-attachments/assets/0f321c81-d4a7-4ae3-b617-002d15c7a1f9)
![imagen](https://github.com/user-attachments/assets/c2864878-b165-407f-876e-fdb3040883a5)



## How does it work
Inspired by Linguisticae's [video](https://www.youtube.com/watch?v=LsxCzZOqZmI).

This project shows that, while LLMs are not good enough to make fully fledged constructed languages, pairing their generative abilities with symbolic calculation is enough to make interesting experiments.
In this case, the LLM is required to generate a YAML file which contains
1. A list of word roles and corresponding morphosyntaxic regex
2. A context-free grammar to manage sentence creation and word order
3. A list of transliteration rules to convert the sentences to IPA

## How to use

1. The prompt can be found [here](prompt.txt). Simply copy-paste it inside a LLM chat bot.
You should then talk with the agent to ask it to change the grammar the alphabet or anything about the language.
You can use the transliteration for converting to other alphabets too :)

2. Download the [main](main.py) python file and install dependencies `pip install argparse exrex`
3. Then copy-paste the generated YAML to a file and you can try your language with
`python main.py MYFILE.yaml`

Feel free to share your language creations in [examples](/examples) (right now examples are pretty bad lol).

## Contributing
This is a fun one day experiment project and it's thus quite a bit limited.

Here are some possible improvements:
- Improve the prompt (please)
- Use grammars intead of regular languages for word roles, for example detail vowel consonants patterns such as CVCV
- Use context-dependent grammars for sentence creation
- Use a finite-state transductor for transliteration
- Implement word inflexion (conjugation, case, number, gender, etc.)

If you want to improve the project, feel free to PR.
