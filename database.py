from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config import DB_URL
from models import Base

engine = create_engine(DB_URL, echo=True)
SessionLocal = scoped_session(sessionmaker(bind=engine))

def init_db():
    Base.metadata.create_all(bind=engine)

def test_db_content():
    """Проверяет, что сессия читает данные из БД"""
    session = get_session()
    try:
        # Считаем записи в каждой таблице
        from models import User, Product, Order
        print(f"👥 Пользователей: {session.query(User).count()}")
        print(f"👟 Товаров: {session.query(Product).count()}")
        print(f"📦 Заказов: {session.query(Order).count()}")
        return True
    except Exception as e:
        print(f"❌ Ошибка при чтении: {e}")
        return False
    finally:
        session.close()

def get_session():
    return SessionLocal()
