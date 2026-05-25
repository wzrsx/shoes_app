from pathlib import Path

DB_URL = "postgresql+psycopg2://postgres:q1w2e3@localhost:5432/demo"

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "images"
RESOURCES_DIR = BASE_DIR / "resources"
PLACEHOLDER_IMAGE = RESOURCES_DIR / "picture1.jpg"

COLOR_DISCOUNT = "#2E8B57"
COLOR_OUT_OF_STOCK = "#87CEEB"
COLOR_OLD_PRICE = "red"
COLOR_SELECTED_CARD = "#B9B9B9"

ROLE_GUEST = "guest"
ROLE_CLIENT = "client"
ROLE_MANAGER = "manager" 
ROLE_ADMIN = "admin"

