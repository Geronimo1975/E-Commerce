from datetime import datetime

class Review:
    def __init__(self, rating: int, comment: str, user_name: str = "Anonymous"):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self.rating = rating
        self.comment = comment
        self.user_name = user_name
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            'rating': self.rating,
            'comment': self.comment,
            'user_name': self.user_name,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.reviews = []

    def add_review(self, rating: int, comment: str, user_name: str = "Anonymous"):
        review = Review(rating, comment, user_name)
        self.reviews.append(review)

    def get_average_rating(self):
        if not self.reviews:
            return None
        return sum(review.rating for review in self.reviews) / len(self.reviews)

    def get_reviews(self):
        return [review.to_dict() for review in self.reviews]

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_product_info(self):
        avg_rating = self.get_average_rating()
        rating_str = f", Rating: {avg_rating:.1f}★" if avg_rating is not None else ""
        return f"Product: {self.name}, Price: {self.price:.2f}€, Quantity: {self.quantity}{rating_str}"