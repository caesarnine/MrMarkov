from collections import defaultdict
import random

def markov(text, order, num_sentences, rand, seed):
    corpus = generate_dict(text,order)
    return generate_text(corpus, num_sentences, rand, order, seed)

def generate_dict(text,order):
    d = defaultdict(list)
    words = text.split()
    for i, word in enumerate(words):
        gs = []
        try:
            for j in range(0,order+1):
                gs.append(words[i+j])
        except:
            break
        d[tuple(gs[:-1])].append(gs[-1])
    return d

def generate_text(corpus, num_sentences, rand, order=2, seed=[]):
    gen_text = []
    if rand == True:
        start = [key for key in corpus.keys() if key[0][0].isupper()]
        seed = random.choice(start)    
    gen_text.append(' '.join(seed))
    #print 1,gen_text
    sentences=0
    while True:
        seed = tuple(seed)
        try:
            text = random.choice(corpus[seed])
            gen_text.append(text)
            if ' '.join(gen_text)[-1] in ['!','?','.']:
                sentences += 1
                #print sentences
                if sentences >= num_sentences:
                    break;
            seed = seed[-order+1:] + tuple([text])
            #print 2, seed
        except:
            break;
    return ' '.join(gen_text)

