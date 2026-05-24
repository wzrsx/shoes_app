#!/usr/bin/env python3
"""
Наполнение БД тестовыми данными
Совместимо с вашей схемой из pgAdmin
"""

from datetime import datetime, timedelta
from database import get_session, init_db
from models import User, Product, Order, OrderItem, Delivery
from config import ROLE_ADMIN, ROLE_CLIENT, ROLE_MANAGER

def seed():
    session = get_session()
    try:
        print("🌱 Наполнение базы тестовыми данными...")

        # ==================== ПОЛЬЗОВАТЕЛИ ====================
        users = [
            User(
                login="admin", password="admin123", role=ROLE_ADMIN,
                name="Администратор", fio="Админ Админович"
            ),
            User(
                login="manager", password="mgr123", role=ROLE_MANAGER,
                name="Менеджер", fio="Менеджер Менеджерович"
            ),
            User(
                login="client", password="clt123", role=ROLE_CLIENT,
                name="Клиент", fio="Клиент Клиентович"
            ),
        ]
        session.add_all(users)
        session.flush()  # Фиксируем, чтобы получить user.id
        print(f"✓ Создано пользователей: {len(users)}")

        # ==================== ТОВАРЫ ====================
        # Важно: article — это PRIMARY KEY, задаём вручную
        products = [
            Product(
                article="NIKE-AIR-001",  # ← строка, не autoincrement!
                title="Кроссовки Nike Air Max",
                measure_type="пара",
                price=8990.00,
                discount=10.0,  # double precision
                quantity=25,
                category="Спорт",
                supplier="Nike RU",
                producer="Nike Inc.",
                description="Лёгкие беговые кроссовки с амортизацией",
                image_url=""
            ),
            Product(
                article="BOOT-WINTER-002",
                title="Ботинки зимние кожаные",
                measure_type="пара",
                price=12500.00,
                discount=0.0,
                quantity=8,
                category="Зима",
                supplier="ОбувьОпт",
                producer="Локальный цех",
                description="Натуральная кожа, утеплитель, рифлёная подошва",
                image_url=""
            ),
            Product(
                article="SANDAL-SUMMER-003",
                title="Сандалии летние",
                measure_type="пара",
                price=3490.00,
                discount=15.0,
                quantity=40,
                category="Лето",
                supplier="ЛетоОбувь",
                producer="Fashion Shoes Ltd",
                description="Дышащие материалы, удобная колодка",
                image_url=""
            ),
        ]
        session.add_all(products)
        session.flush()
        print(f"✓ Создано товаров: {len(products)}")

        # ==================== ДОСТАВКА ====================
        deliveries = [
            Delivery(address="г. Москва, ул. Тверская, д. 1, кв. 10"),
            Delivery(address="г. Санкт-Петербург, Невский пр., д. 25"),
            Delivery(address="г. Казань, ул. Баумана, д. 5"),
        ]
        session.add_all(deliveries)
        session.flush()
        print(f"✓ Создано адресов доставки: {len(deliveries)}")

        # ==================== ЗАКАЗЫ ====================
        # Находим пользователя-клиента
        client = session.query(User).filter(User.login == "client").first()
        
        orders = [
            Order(
                user_id=client.id,
                order_date=datetime.now().date(),
                delivery_date=(datetime.now() + timedelta(days=3)).date(),
                address_id=deliveries[0].id,
                challenge_code=782341,  # ← integer, не строка!
                status="new"
            ),
            Order(
                user_id=client.id,
                order_date=(datetime.now() - timedelta(days=5)).date(),
                delivery_date=(datetime.now() - timedelta(days=2)).date(),
                address_id=deliveries[1].id,
                challenge_code=451092,
                status="delivered"
            ),
        ]
        session.add_all(orders)
        session.flush()
        print(f"✓ Создано заказов: {len(orders)}")

        # ==================== ПОЗИЦИИ ЗАКАЗА ====================
        # Важно: article — это строка из Product, а не ID!
        order_items = [
            # Заказ 1: 2 позиции
            OrderItem(
                order_id=orders[0].id,
                article="NIKE-AIR-001",  # ← строка-артикул!
                quantity=1
            ),
            OrderItem(
                order_id=orders[0].id,
                article="SANDAL-SUMMER-003",
                quantity=2
            ),
            # Заказ 2: 1 позиция
            OrderItem(
                order_id=orders[1].id,
                article="BOOT-WINTER-002",
                quantity=1
            ),
        ]
        session.add_all(order_items)
        print(f"✓ Создано позиций заказа: {len(order_items)}")

        # ==================== ФИНАЛ ====================
        session.commit()
        
        # Итоговая статистика
        print("\n🎉 База успешно наполнена!")
        print(f"   • Пользователей: {session.query(User).count()}")
        print(f"   • Товаров: {session.query(Product).count()}")
        print(f"   • Заказов: {session.query(Order).count()}")
        print(f"   • Позиций в заказах: {session.query(OrderItem).count()}")
        
        print("\n🔑 Данные для входа:")
        print("   • Админ:    admin / admin123")
        print("   • Менеджер: manager / mgr123")
        print("   • Клиент:   client / clt123")
        
        print("\n📦 Пример заказа:")
        order = session.query(Order).first()
        items = session.query(OrderItem).filter(OrderItem.order_id == order.id).all()
        print(f"   Заказ #{order.id} от {order.order_date}:")
        for item in items:
            prod = session.query(Product).filter(Product.article == item.article).first()
            print(f"     • {prod.title} (арт. {item.article}) × {item.quantity}")

    except Exception as e:
        session.rollback()
        print(f"\n❌ Ошибка при наполнении: {type(e).__name__}: {e}")
        raise
    finally:
        session.close()
        print("\n✅ Сессия закрыта")


if __name__ == "__main__":
    # Создаём таблицы, если их нет (безопасно для существующих данных)
    init_db()
    seed()