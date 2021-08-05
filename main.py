import json
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, FastAPI, HTTPException

import query_builder
from model import Recipe

con = sqlite3.connect('recipes.db')
cur = con.cursor()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://superpuperrecipeapp.web.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/recipes")
async def add_recipe(recipe: Recipe):
    if len(recipe.steps) > 0 and recipe.steps[-1]  == "Будет вкусно!":
        last_id = query_builder.insert_recipe(cur, con, recipe)
        return last_id
    else:
        raise HTTPException(status_code=401, detail="Вы посторонний человек")

@app.delete("/recipes/{id}")
async def delete_recipe(id):
    query_builder.delete_recipe(cur, con, id)
    return "OK"

@app.get("/recipes")
async def get_recipes():
    return query_builder.get_recipes(cur)
