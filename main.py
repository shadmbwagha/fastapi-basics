from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'title one', 'author': 'Author One'},
    'book_2': {'title': 'title two', 'author': 'Author Two'},
    'book_3': {'title': 'title three', 'author': 'Author Three'},
    'book_4': {'title': 'title four', 'author': 'Author Four'},
    'book_5': {'title': 'title five', 'author': 'Author Five'}
}

@app.get('/')
async def read_all_books():
    return BOOKS

@app.get('/books/{book_name}')
async def read_book(book_name: str):
    return BOOKS[book_name]

class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"

@app.get('/directions/{direction_name}')
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "up"}
    elif direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "down"}
    elif direction_name == DirectionName.east:
        return {"Direction": direction_name, "sub": "right"}
    else:
        return {"Direction": direction_name, "sub": "left"}
