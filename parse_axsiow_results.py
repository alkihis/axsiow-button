# -*- coding: utf-8 -*-
import json
import sys


def show_stats(data):
    counts = {}
    total_count = data['count']
    comments = data['comments']

    for reason in comments.values():
        described_reason = meanings.get(reason, reason)

        if described_reason in counts:
            counts[described_reason] += 1
        else:
            counts[described_reason] = 1

    reasons = list(counts.items())
    reasons.sort(key=lambda x: x[1], reverse=True)

    print('Nombre d\'appuis sur le bouton : ' + str(total_count))
    print('\nRaisons d\'appui sur le bouton :')

    for reason, count in reasons:
        print('  - ' + reason + ' : ' + str(count))


meanings = {
    '__grenoble__': 'Grenoble',
    '__piolle__': 'Éric Piolle',
    '__sex__': 'Le cul',
    '__devs__': 'Les devs, ces merdes',
    '__network__': 'Le réseau c\'est mieux',
    '__argot__': 'Argot grenoblois',
    '__hugues__': 'Hot take sur le ski',
    '__jmlp__': 'Sortie xénophobe',
    '__macron__': 'Random truc de droite',
    '__noix__': 'Hot take sur la bouffe',
    '__marseille__': 'Exagération sur un sujet aléatoire',
}

if sys.version_info < (3,0):
    # stdin is bytes in Python 2, not str
    import codecs
    axsiow_data = json.load(codecs.getreader('utf-8')(sys.stdin))
else:
    axsiow_data = json.load(sys.stdin)

show_stats(axsiow_data)
