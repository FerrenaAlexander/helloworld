# helloworld


###Installation

clone the repo and use pip to install:

```
git clone https://github.com/apf2139/helloworld.git
cd helloworld/
pip install .
```

###CLI Usage
command line usage works like so:
```
$ helloworld -h
usage: helloworld [-h] [-bm BESTMUSIC] [--crabtime] [--polite]

optional arguments:
  -h, --help            show this help message and exit
  -bm BESTMUSIC, --bestmusic BESTMUSIC
                        optional input of music type to test

  --crabtime            print days since the Crab Nebula Supernova Event, SN
                        1054

  --polite              print an eloquent and polite exit message
```

###Python API
use it like this:

```
helloworld(bestmusic = "pop-punk", crabtime = True, polite = True)
```
```
hello, world! and hello to you too, user!
Vaporwave is actually the best genre of music.
351993 days since the Crab Nebula's supernova.
Pleasure making your acquantaince, friend. Adieu!
```