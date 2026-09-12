from sqlalchemy import (
    Column, Integer, String, ForeignKey, Text, Float, DateTime, UniqueConstraint
)
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    year = Column(Integer)
    description = Column(Text)
    poster_url = Column(String(500))

    recipes = relationship("Recipe", back_populates="movie", cascade="all, delete-orphan")
    soundtracks = relationship("Soundtrack", back_populates="movie", cascade="all, delete-orphan")


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False, index=True)


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    instructions = Column(Text)
    cooking_time = Column(Integer)
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))

    movie = relationship("Movie", back_populates="recipes")
    ingredients = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    amount = Column(Float)
    unit = Column(String(20))

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient")


class Soundtrack(Base):
    __tablename__ = "soundtracks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    file_url = Column(String(500), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))

    movie = relationship("Movie", back_populates="soundtracks")