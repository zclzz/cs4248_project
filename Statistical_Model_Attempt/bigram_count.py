import nltk 
from tqdm import tqdm
from collections import defaultdict
from nltk.tokenize import word_tokenize

# Helper methods
def apply_edits(sentence, edits):
    # Sort edits by start position in reverse order
    sentence = sentence.split(" ")
    edits_sorted = sorted(edits, key=lambda x: x[0], reverse=True)
    for edit in edits_sorted:
        start = int(edit[0])
        end = int(edit[1])
        replacement = edit[2].strip()
        sentence = sentence[:start] + [replacement] + sentence[end:]
    return ' '.join(sentence)

bigram_count = defaultdict(int)

# Do not apply edits with these error types
skip = {"noop", "UNK", "Um"}

# Main logic 
training_file = open("ABC.train.gold.bea19.m2")
output_file = open("bigram_stats.txt", "w")
training_data = training_file.readlines()

sentence_edits = [] # Populate the sentence edits for sorting
wrong_sentence = "" # Temp variable for the wrong sentece
correct_sentence = "" # Temp variable for the correct sentence

for line in tqdm(training_data):
    if line[0] == "S":
        # Strip the S 
        wrong_sentence = line[2:].strip()
    elif line[0] == "A":
        edits = line[2:].split("|||")
        # Ignore edits
        if edits[1] in skip:
            continue
        start, end = edits[0].split(" ")
        changes = edits[2]
        sentence_edits.append([start, end, changes])
    else:
        # If we reach here then it is sure that all the edits 
        # have been populated
        correct_sentence = apply_edits(wrong_sentence, sentence_edits)
        correct_sentence_tokens = word_tokenize(correct_sentence)
        correct_sentence_tokens = ["<start>"] + correct_sentence_tokens + ["<end>"]
        bigrams = nltk.bigrams(correct_sentence_tokens)
        for bigram in bigrams:
            bigram_count[bigram] += 1 
        
        # Flush old values 
        sentence_edits = []
        wrong_sentence = ""
        correct_sentence = ""

bigram_count = dict(sorted(bigram_count.items(), key=lambda item: item[1], reverse=True))

for key, value in bigram_count.items():
    output_file.write(str(key) + " " + str(value) + "\n")