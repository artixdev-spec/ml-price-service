from pydantic import BaseModel


class ProductInput(BaseModel):
    """Схема входных данных для предсказания цены."""
    
    weight: float  # вес в кг
    category: int  # категория товара (1-5)
    rating: float  # рейтинг (0-5)
    reviews_count: int  # количество отзывов

    class Config:
        json_schema_extra = {
            "example": {
                "weight": 2.5,
                "category": 3,
                "rating": 4.2,
                "reviews_count": 150
            }
        }


class PricePrediction(BaseModel):
    """Схема ответа с предсказанной ценой."""
    
    predicted_price: float
    currency: str = "RUB"
    model_version: str = "1.0.0"
