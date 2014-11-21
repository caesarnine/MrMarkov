import os
# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
if os.environ.get('PORT'):
    # We're hosted on Heroku! Use the MongoHQ sandbox as our backend.
    MONGO_HOST = ''
    MONGO_PORT = 
    MONGO_USERNAME = ''
    MONGO_PASSWORD = ''
    MONGO_DBNAME = ''

    SERVER_NAME = ''
else:
    # Running on local machine. Let's just use the local mongod instance.

    # Please note that MONGO_HOST and MONGO_PORT could very well be left
    # out as they already default to a bare bones local 'mongod' instance.
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = 'username'
    MONGO_PASSWORD = 'password'
    MONGO_DBNAME = 'apitest'



EXTRA_RESPONSE_FIELDS = ['generated_text']

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'original_text': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 3000,
    },
    'generated_text': {
        'type': 'string',
    },
}

text = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'text',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

DOMAIN = {
    'text': text,
}


