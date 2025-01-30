import exrex
import random
import re
import yaml
import argparse

# Function to load the YAML data
def load_language_data(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to generate words based on role and regex
def generate_words(role_regex, max_words=10, max_word_length=8):
    return list({exrex.getone(role_regex, limit=max_word_length) for _ in range(max_words)})

# Function to generate a sentence from grammar rules
def generate_sentence(grammar_rules, word_bank, max_use=3):
    use_count = {symbol: 0 for symbol in grammar_rules}

    def expand_symbol(symbol):        
        if symbol.startswith('@'):
            role = symbol[1:]
            if role in word_bank:
                return random.choice(word_bank[role])
            return symbol
        
        rule = grammar_rules.get(symbol)
        if rule:
            valid_rules = [s for s in rule if use_count.get(s, 0) < max_use]
            chosen_rule = random.choice(valid_rules)
            expanded_parts = []
            for part in chosen_rule.split():
                if symbol in grammar_rules:
                    use_count[symbol] += 1
                expanded_parts.append(expand_symbol(part))
            
            return ' '.join(expanded_parts)
        
        return symbol

    return expand_symbol('S')

# Function to apply IPA rules to a sentence
def apply_phonetic_rules(sentence, phonetic_rules):
    for rule in phonetic_rules:
        sentence = re.sub(rule['pattern'], rule['replace'], sentence)
    return sentence

# Main function to orchestrate the process
def generate_conlang(file_path):
    # Load the YAML file
    language_data = load_language_data(file_path)

    language_name = language_data['language']['name']
    word_roles = language_data['word_roles']
    grammar_rules = language_data['grammar_rules']
    phonetic_rules = language_data['phonetic_rules']

    print(f"Bienvenue sur neo-lang!\nÉtudions cette langue: {language_name}\n===========================\n")

    word_bank = {}
    for role, regex in word_roles.items():
        word_bank[role] = generate_words(regex, 10)
        print(f"Mots générés de type {role}: {word_bank[role]}")

    print("\nPhrases d'exemples:")
    for i in range(15):
        sentence = generate_sentence(grammar_rules, word_bank)
        sentence_ipa = apply_phonetic_rules(sentence, phonetic_rules)

        print(f'{i+1}. {sentence}\n{(len(str(i+1))+2)*" "}{sentence_ipa}\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate conlang from a YAML file.")
    parser.add_argument('filename', type=str, help="Path to the YAML file")
    args = parser.parse_args()

    generate_conlang(args.filename)
