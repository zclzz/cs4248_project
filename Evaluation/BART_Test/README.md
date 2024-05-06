# Steps to reproduce

## For all (steps for original dataset is the same)

- Run `bart_test_additional.ipynb` to get the system output.

## ERRANT

- Change directory to `BART_Test`
- Run `errant_parallel -orig ../ABCN_dev_source.txt -cor bart_output_additional.txt -out bart_additional.m2`
- Run `errant_compare -hyp bart_additional.m2 -ref ../ABCN.dev.gold.bea19.m2 -cat 3`

## GLEU

- Change directory to `Evaluation`
- Run `python2 gleu/complete_gleu.py -s ABCN_dev.src -r ABCN_dev.trg -o BART_Test/bart_output_additional.txt -d`

## M2 Score

- Change directory to `Evaluation`
- Run `python2 m2_score/m2_scorer.py BART_Test/bart_output_additional.txt ABCN.dev.gold.bea19.m2`


# Output - Additional Dataset

## ERRANT

```
===================== Span-Based Correction ======================
Category       TP       FP       FN       P        R        F0.5
M:ADJ          0        2        15       0.0      0.0      0.0
M:ADV          0        8        27       0.0      0.0      0.0
M:CONJ         0        2        25       0.0      0.0      0.0
M:CONTR        0        0        2        1.0      0.0      0.0
M:DET          0        13       359      0.0      0.0      0.0
M:NOUN         0        180      26       0.0      0.0      0.0
M:NOUN:POSS    0        67       27       0.0      0.0      0.0
M:OTHER        0        9        90       0.0      0.0      0.0
M:PART         0        1        11       0.0      0.0      0.0
M:PREP         0        10       148      0.0      0.0      0.0
M:PRON         0        3        67       0.0      0.0      0.0
M:PUNCT        21       129      1069     0.14     0.0193   0.0621
M:VERB         1        10       40       0.0909   0.0244   0.0588
M:VERB:FORM    0        1        21       0.0      0.0      0.0
M:VERB:TENSE   0        1        60       0.0      0.0      0.0
R:ADJ          13       53       73       0.197    0.1512   0.1857
R:ADJ:FORM     9        1        7        0.9      0.5625   0.8036
R:ADV          8        27       54       0.2286   0.129    0.198
R:CONJ         0        1        8        0.0      0.0      0.0
R:CONTR        1        12       18       0.0769   0.0526   0.0704
R:DET          40       47       118      0.4598   0.2532   0.3953
R:MORPH        48       45       110      0.5161   0.3038   0.4528
R:NOUN         28       162      238      0.1474   0.1053   0.1365
R:NOUN:INFL    1        0        9        1.0      0.1      0.3571
R:NOUN:NUM     117      91       134      0.5625   0.4661   0.5402
R:NOUN:POSS    1        152      28       0.0065   0.0345   0.0078
R:ORTH         116      746      236      0.1346   0.3295   0.1526
R:OTHER        77       1964     765      0.0377   0.0914   0.0427
R:PART         17       9        25       0.6538   0.4048   0.5822
R:PREP         185      158      301      0.5394   0.3807   0.4978
R:PRON         23       35       41       0.3966   0.3594   0.3885
R:PUNCT        45       210      238      0.1765   0.159    0.1727
R:SPELL        13       269      374      0.0461   0.0336   0.0429
R:VERB         48       192      284      0.2      0.1446   0.1858
R:VERB:FORM    83       54       120      0.6058   0.4089   0.5526
R:VERB:INFL    1        0        4        1.0      0.2      0.5556
R:VERB:SVA     105      62       43       0.6287   0.7095   0.6434
R:VERB:TENSE   97       102      274      0.4874   0.2615   0.4156
R:WO           0        5        95       0.0      0.0      0.0
U:ADJ          1        0        11       1.0      0.0833   0.3125
U:ADV          0        3        26       0.0      0.0      0.0
U:CONJ         0        3        11       0.0      0.0      0.0
U:CONTR        0        0        9        1.0      0.0      0.0
U:DET          7        7        272      0.5      0.0251   0.1045
U:NOUN         1        7        35       0.125    0.0278   0.0735
U:NOUN:POSS    0        0        10       1.0      0.0      0.0
U:OTHER        0        7        48       0.0      0.0      0.0
U:PART         0        1        7        0.0      0.0      0.0
U:PREP         5        8        101      0.3846   0.0472   0.1582
U:PRON         3        6        44       0.3333   0.0638   0.1807
U:PUNCT        4        4        101      0.5      0.0381   0.146
U:VERB         1        1        28       0.5      0.0345   0.1351
U:VERB:FORM    0        0        12       1.0      0.0      0.0
U:VERB:TENSE   0        2        42       0.0      0.0      0.0

=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
1120    4882    6341    0.1866  0.1501  0.178
==============================================
```

## GLEU

```
Score = 0.706833
```

## M2 Score

```
Precision   : 0.3729
Recall      : 0.3096
F_0.5       : 0.3583
```

# Output - Original Dataset

## ERRANT

```
===================== Span-Based Correction ======================
Category       TP       FP       FN       P        R        F0.5
M:ADJ          0        5        15       0.0      0.0      0.0
M:ADV          0        10       27       0.0      0.0      0.0
M:CONJ         0        2        25       0.0      0.0      0.0
M:CONTR        0        0        2        1.0      0.0      0.0
M:DET          1        11       358      0.0833   0.0028   0.0123
M:NOUN         0        222      26       0.0      0.0      0.0
M:NOUN:POSS    0        65       27       0.0      0.0      0.0
M:OTHER        1        18       89       0.0526   0.0111   0.0301
M:PART         0        1        11       0.0      0.0      0.0
M:PREP         0        11       148      0.0      0.0      0.0
M:PRON         0        3        67       0.0      0.0      0.0
M:PUNCT        21       616      1069     0.033    0.0193   0.0289
M:VERB         1        10       40       0.0909   0.0244   0.0588
M:VERB:FORM    0        0        21       1.0      0.0      0.0
M:VERB:TENSE   0        2        60       0.0      0.0      0.0
R:ADJ          15       53       71       0.2206   0.1744   0.2095
R:ADJ:FORM     7        1        9        0.875    0.4375   0.7292
R:ADV          7        38       55       0.1556   0.1129   0.1446
R:CONJ         0        2        8        0.0      0.0      0.0
R:CONTR        1        12       18       0.0769   0.0526   0.0704
R:DET          37       45       121      0.4512   0.2342   0.3807
R:MORPH        40       46       118      0.4651   0.2532   0.3984
R:NOUN         34       179      232      0.1596   0.1278   0.1521
R:NOUN:INFL    1        0        9        1.0      0.1      0.3571
R:NOUN:NUM     127      109      124      0.5381   0.506    0.5314
R:NOUN:POSS    1        154      28       0.0065   0.0345   0.0077
R:ORTH         124      736      228      0.1442   0.3523   0.1635
R:OTHER        82       2128     760      0.0371   0.0974   0.0423
R:PART         18       15       24       0.5455   0.4286   0.5172
R:PREP         193      167      293      0.5361   0.3971   0.501
R:PRON         22       31       42       0.4151   0.3438   0.3986
R:PUNCT        49       219      234      0.1828   0.1731   0.1808
R:SPELL        17       263      370      0.0607   0.0439   0.0564
R:VERB         53       191      279      0.2172   0.1596   0.2026
R:VERB:FORM    86       54       117      0.6143   0.4236   0.5636
R:VERB:INFL    2        2        3        0.5      0.4      0.4762
R:VERB:SVA     107      70       41       0.6045   0.723    0.625
R:VERB:TENSE   101      87       270      0.5372   0.2722   0.4497
R:WO           0        10       95       0.0      0.0      0.0
U:ADJ          1        2        11       0.3333   0.0833   0.2083
U:ADV          0        4        26       0.0      0.0      0.0
U:CONJ         0        5        11       0.0      0.0      0.0
U:CONTR        0        0        9        1.0      0.0      0.0
U:DET          7        8        272      0.4667   0.0251   0.1032
U:NOUN         1        8        35       0.1111   0.0278   0.0694
U:NOUN:POSS    0        0        10       1.0      0.0      0.0
U:OTHER        0        8        48       0.0      0.0      0.0
U:PART         0        0        7        1.0      0.0      0.0
U:PREP         7        9        99       0.4375   0.066    0.2059
U:PRON         2        7        45       0.2222   0.0426   0.1205
U:PUNCT        5        4        100      0.5556   0.0476   0.1773
U:VERB         0        1        29       0.0      0.0      0.0
U:VERB:FORM    0        0        12       1.0      0.0      0.0
U:VERB:TENSE   2        3        40       0.4      0.0476   0.1613

=========== Span-Based Correction ============
TP      FP      FN      Prec    Rec     F0.5
1173    5647    6288    0.172   0.1572  0.1688
==============================================
```

## GLEU

```
Score = 0.708916
```

## M2 Score

```
Precision   : 0.3497
Recall      : 0.3252
F_0.5       : 0.3445
```

# Output - Prefix with Original Data

## ERRANT

```

```

## GLEU

```

```

## M2 Score

