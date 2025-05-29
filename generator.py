"""
xianxia_quotes

A small utility to generate xianxia-style proverbs, e.g.:
    “Even a dragon will lose to a snake in its lair”
"""

import random

# Constants: lists of terms used to build each proverb
ANIMALS = [
    "dragon", "tiger", "lion", "serpent", "fox", "wolf", "eagle", "panther",
    "bear", "phoenix", "hare", "crane", "crow", "hawk", "monkey", "elephant",
    "rhinoceros", "leopard", "cobra", "stallion", "boar", "otter", "falcon",
    "lynx", "jaguar", "camel", "mongoose", "buffalo", "yak", "stag", "manticore",
    "gryphon", "kraken", "wyvern", "unicorn", "basilisk", "chimera",
    "hippopotamus", "puma", "moth", "stingray", "orca", "gazelle", "badger",
    "mantis", "koala", "platypus", "narwhal", "lemur", "tapir", "armadillo",
    "porcupine", "peacock", "vulture", "tarantula", "seahorse", "ostrich"
]

CONTEXTS = [
    "in its lair", "in the mountain", "in the forest", "in the sky", "at dawn",
    "at dusk", "under the moon", "under the sun", "by the river", "on the desert",
    "in the mist", "in the storm", "near the abyss", "on the ridge",
    "at high tide", "in the valley", "on the cliff", "in the swamp",
    "at the crossroads", "in the canyon", "on the ice", "in the jungle",
    "beneath the waves", "among the reeds", "within the volcano",
    "at the waterfall", "on the floating isle", "in the shadow",
    "along the caravan trail", "at the mountain pass", "within the palace",
    "on the battlements", "beside the ancient ruins", "under the glacier",
    "amid the ruins", "within the labyrinth", "by the geyser", "on the salt flats",
    "in the wind-swept plains"
]

VERBS = [
    "lose to", "bow before", "fall to", "be humbled by", "be outmatched by",
    "yield to", "falter before", "submit to", "be overshadowed by",
    "be outfoxed by", "be outpaced by", "be outmaneuvered by", "respect",
    "cower before", "be surprised by", "be bested by", "be tricked by",
    "be ensnared by", "be dethroned by", "be outwitted by", "be outclassed by",
    "be dominated by", "be flanked by", "be overpowered by",
    "be outmatched in strength by", "be confounded by", "be unseated by",
    "be eclipsed by", "be outplayed by", "be overrun by", "be startled by",
    "be cornered by", "be outworked by", "be checked by", "be silenced by"
]


def quote_stream():
    """
    An infinite generator of xianxia-style proverbs.

    Yields:
        str: A proverb of the form:
             “Even a {animal1} will {verb} a {animal2} {context}”
    """
    while True:
        subject, target = random.sample(ANIMALS, 2)
        verb = random.choice(VERBS)
        context = random.choice(CONTEXTS)
        yield f"“Even a {subject} will {verb} a {target} {context}”"


def single_quote():
    """
    Return a single xianxia-style proverb.
    """
    return next(quote_stream())


def main():
    """
    Entry point: print one random proverb.
    """
    print(single_quote())


if __name__ == "__main__":
    main()
