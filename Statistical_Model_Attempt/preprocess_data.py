import spacy 
from tqdm import tqdm

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

# Do not apply edits with these error types
skip = {"noop", "UNK", "Um"}

# Main logic 
nlp = spacy.load("en_core_web_trf")
training_file = open("ABC.train.gold.bea19.m2")
output_file = open("output.txt", "w")
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
        processed_wrong_sentence = nlp(wrong_sentence)
        processed_correct_sentence = nlp(correct_sentence)

        wrong_noun_phrases = [chunk.text for chunk in processed_wrong_sentence.noun_chunks]
        correct_noun_phrases = [chunk.text for chunk in processed_correct_sentence.noun_chunks]
        
        # Write to a file
        output_file.write(wrong_sentence + "\n")
        output_file.write(correct_sentence + "\n")
        output_file.write(str(wrong_noun_phrases) + "\n")
        output_file.write(str(correct_noun_phrases) + "\n")

        # Flush old values 
        sentence_edits = []
        wrong_sentence = ""
        correct_sentence = ""

output_file.close()