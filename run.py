from eve import Eve
from markov_code import markov
import os

def add_sentence(resource, response):
    response[0]['generated_text'] = markov(response[0]['original_text'], order=2, num_sentences=2, rand=True,seed=[])

app = Eve()
app.on_insert += add_sentence

if __name__ == '__main__':
    # Heroku support: bind to PORT if defined, otherwise default to 5000.
    if 'PORT' in os.environ:
        port = int(os.environ.get('PORT'))
        # use '0.0.0.0' to ensure your REST API is reachable from all your
        # network (and not only your computer).
        host = '0.0.0.0'
    else:
        port = 5000
        host = '127.0.0.1'

    app.run(host=host, port=port)
