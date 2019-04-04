from graphql_demo import app
from graphql_demo.schema import schema
from flask_graphql import GraphQLView


@app.route('/')
def index():
    return '<p> Hello World</p>'


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)
