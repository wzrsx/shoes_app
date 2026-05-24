# models.py — SQLAlchemy модели (точно как в вашей БД)
from sqlalchemy import Column, Integer, String, Double, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    role = Column(String, nullable=False)
    name = Column(String, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    fio = Column(Text)


class Delivery(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)


class Product(Base):
    __tablename__ = 'product'
    article = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    measure_type = Column(String, nullable=False)
    price = Column(Double, nullable=False)
    supplier = Column(String, nullable=False)
    producer = Column(String, nullable=False)
    category = Column(String, nullable=False)
    discount = Column(Double, nullable=False, default=0.0)
    quantity = Column(Integer, nullable=False, default=0)
    description = Column(Text)
    image_url = Column(String)


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False)
    delivery_date = Column(Date)
    address_id = Column(Integer, ForeignKey('delivery.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    challenge_code = Column(Integer, nullable=False)
    status = Column(String, nullable=False)


class OrderItem(Base):
    __tablename__ = 'orderitem'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    article = Column(String, ForeignKey('product.article'), nullable=False)
    quantity = Column(Integer, nullable=False)