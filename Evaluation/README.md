# Evaluation of GEC 

Three metrics are used (which are the best practices):

- [M^2 Scorer](https://github.com/nusnlp/m2scorer/tree/master)
- [GLEU Metric](https://github.com/cnap/gec-ranking/tree/master)
- [ERRANT](https://github.com/chrisjbryant/errant)

# Installation Requirements

```
python2 - scipy
python3
```

# Commands to run

## M^2 Scorer

```bash
python2 m2_score/m2_scorer.py [OPTIONS] SYSTEM SOURCE_GOLD`
```

```
SYSTEM - system output, one sentence per line
SOURCE_GOLD - source sentences with gold token edits
OPTIONS
  -v    --verbose             -  print verbose output
  --very_verbose              -  print lots of verbose output
  --max_unchanged_words N     -  Maximum unchanged words when extracting edits. Default = 2.
  --ignore_whitespace_casing  -  Ignore edits that only affect whitespace and casing. Default no.
  --beta 
```

### System output format

The sentences should be in tokenized plain text, sentence-per-line format.

```
<tokenized system output for sentence 1>
<tokenized system output for sentence 2>
...
```

Examples of tokenization:
Original: He said, "We shouldn't go to the place. It'll kill one of us."
Tokenized: He said , " We should n't go to the place . It 'll kill one of us . "

**Note**: Tokenization in the CoNLL-2014 shared task uses NLTK word tokenizer.

### Example command

`python2 m2_score/m2_scorer.py m2_score/example/system m2_score/example/source_gold`



## GLEU

```bash
python2 gleu/complete_gleu.py -s source_sentences -r reference [reference ...] \
        -o system_output [system_output ...] -n 4 -l 0.0
```

where each file contains one sentence per line. GLEU can be run with multiple references. To get the GLEU scores of multiple outputs, include the path to each system output file. 

## ERRANT

`pip3 install errant`

## Usage

Three main commands are provided with ERRANT: `errant_parallel`, `errant_m2` and `errant_compare`. You can run them from anywhere on the command line without having to invoke a specific python script.  

1. `errant_parallel`  

     This is the main annotation command that takes an original text file and at least one parallel corrected text file as input, and outputs an annotated M2 file. By default, it is assumed that the original and corrected text files are word tokenised with one sentence per line.  
	 Example:
	 ```
	 errant_parallel -orig <orig_file> -cor <cor_file1> [<cor_file2> ...] -out <out_m2>
	 ```

2. `errant_m2`  

     This is a variant of `errant_parallel` that operates on an M2 file instead of parallel text files. This makes it easier to reprocess existing M2 files. You must also specify whether you want to use gold or auto edits; i.e. `-gold` will only classify the existing edits, while `-auto` will extract and classify automatic edits. In both settings, uncorrected edits and noops are preserved.  
     Example:
	 ```
	 errant_m2 {-auto|-gold} m2_file -out <out_m2>
	 ```

3. `errant_compare`  

     This is the evaluation command that compares a hypothesis M2 file against a reference M2 file. The default behaviour evaluates the hypothesis overall in terms of span-based correction. The `-cat {1,2,3}` flag can be used to evaluate error types at increasing levels of granularity, while the `-ds` or `-dt` flag can be used to evaluate in terms of span-based or token-based detection (i.e. ignoring the correction). All scores are presented in terms of Precision, Recall and F-score (default: F0.5), and counts for True Positives (TP), False Positives (FP) and False Negatives (FN) are also shown.  
	 Examples:
	 ```
     errant_compare -hyp <hyp_m2> -ref <ref_m2> 
     errant_compare -hyp <hyp_m2> -ref <ref_m2> -cat {1,2,3}
     errant_compare -hyp <hyp_m2> -ref <ref_m2> -ds
     errant_compare -hyp <hyp_m2> -ref <ref_m2> -ds -cat {1,2,3}
	 ```	

All these scripts also have additional advanced command line options which can be displayed using the `-h` flag. 