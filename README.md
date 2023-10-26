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
$ misspeller mispell "fred" N=4 K=1

["frｅd", "phred", "fr3d", "frd"]
```

## Features

- [x] Homoglyphs
- [x] Leetspeak
- [ ] Soundex (Insert, Drop)
- [ ] Insert (duplicate characters)
- [ ] Drop
- [ ] Swap
- [ ] Short forms: ‘you’ spelled as ‘u’ 


A longer description of your project goes here...


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
