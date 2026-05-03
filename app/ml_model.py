import joblib
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle


class PricePredictor:
    """ML модель для предсказания цены товара."""
    
    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def train(self, X: np.ndarray, y: np.ndarray):
        """Обучение модели."""
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
        
    def predict(self, features: np.ndarray) -> float:
        """Предсказание цены."""
        if not self.is_trained:
            self._load_or_create_model()
        
        features_scaled = self.scaler.transform(features.reshape(1, -1))
        prediction = self.model.predict(features_scaled)
        return float(prediction[0])
    
    def _load_or_create_model(self):
        """Загрузка или создание дефолтной модели."""
        model_path = Path("model.pkl")
        
        if model_path.exists():
            with open(model_path, "rb") as f:
                data = pickle.load(f)
                self.model = data["model"]
                self.scaler = data["scaler"]
                self.is_trained = True
        else:
            # Создаём простую модель с фиктивными коэффициентами
            self._create_dummy_model()
    
    def _create_dummy_model(self):
        """Создание простой модели для демонстрации."""
        # Генерируем синтетические данные для обучения
        np.random.seed(42)
        X = np.random.rand(100, 4) * [10, 5, 5, 500]  # weight, category, rating, reviews
        y = X[:, 0] * 100 + X[:, 1] * 50 + X[:, 2] * 80 + X[:, 3] * 0.5 + np.random.rand(100) * 50
        
        self.train(X, y)
        
        # Сохраняем модель
        model_path = Path("model.pkl")
        with open(model_path, "wb") as f:
            pickle.dump({
                "model": self.model,
                "scaler": self.scaler
            }, f)
        
        self.is_trained = True


# Глобальный экземпляр модели
predictor = PricePredictor()
