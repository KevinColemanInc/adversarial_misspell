# adversarial_misspell

    Library for generating adversial mispellings of words

# Quick Start
## Code

```
from adversarial_misspell import misspeller

# randomly modify the string using any of the modifiers
# N = number of results
# K = max number of modifications

misspeller.refresh() # optional: refreshes modifiers from external data

misspeller.all('fred', N=4, K=1) # ["frｅd", "phred", "fr3d", "frd"]
```

## CLI

Refreshes cache storage

```
$ misspeller refresh
```

Creates 4 misspellings for fred with 1 change in each

```
$ python src/adversarial_misspell/skeleton.py all "fred" 10 1 | jq .
[
  "f>ed",
  "/=red",
  "fred",
  "freI)",
  "fr[-d",
  "fredd",
  "frd",
  "fr℮d",
  "fredd",
  "fed"
]
```

## Features

- [x] Homoglyphs
- [x] Leetspeak
- [x] Insert (duplicate characters)
- [x] Drop
- [x] Swap
- [x] Replace
- [ ] Soundex (Insert, Drop)
- [ ] Short forms: ‘you’ spelled as ‘u’ 
- [ ] Typo (replace with nearby key)


A longer description of your project goes here...


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
