from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from api.query.query import Query

app = FastAPI(
    title="Urban Pulse",
    description="An API which gives you the Traffic and Air Quality Stats",
    version= 1.0
)

schema = strawberry.Schema(query=Query)

app.include_router(GraphQLRouter(schema),prefix="/graphql")

