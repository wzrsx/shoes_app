import sys
import os
import random
from pathlib import Path
from PIL import Image
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem,
    QHeaderView, QComboBox, QAbstractItemView, QMessageBox,
    QFormLayout, QSpinBox, QDoubleSpinBox, QTextEdit, QFileDialog,
    QDateEdit, QDialog
)
from PySide6.QtCore import Qt, QDate, Signal
from PySide6.QtGui import QColor, QBrush, QPixmap

from auth import Ui_LoginWindow
from main_window import Ui_MainWindow
from form import Ui_ProductForm
from product_card import Ui_ProductCard

from config import (
    COLOR_DISCOUNT, COLOR_OUT_OF_STOCK, COLOR_OLD_PRICE,
    ROLE_GUEST, ROLE_CLIENT, ROLE_MANAGER, ROLE_ADMIN,
    IMAGES_DIR, PLACEHOLDER_IMAGE, COLOR_SELECTED_CARD
)
from database import init_db, get_session, test_db_content
from models import User, Product, Order, OrderItem, Delivery

IMAGES_DIR.mkdir(exist_ok=True)

#УТИЛИТЫ

#Изменяет размер изображения и возвращает новый путь
def resize_image(path: str, max_w=300, max_h=200) -> str:
    with Image.open(path) as img:
        img.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)

        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGBA')
            bg = Image.new('RGB', img.size, (255, 255, 255))
            bg.paste(img, mask = img.split()[3])
            img = bg
        
        out_path = IMAGES_DIR / Path(path).name
        img.save(out_path)
        return str(out_path)

#Возвращает путь к изображению или заглушку
def get_image_path(product: Product) -> str:
    if product.image_url and os.path.exists(product.image_url):
        return product.image_url
    return str(PLACEHOLDER_IMAGE) if PLACEHOLDER_IMAGE.exists() else ""

#Показывает сообщение
def show_msg(parent, title: str, text: str, icon=QMessageBox.Information):
    msg = QMessageBox(parent)
    msg.setIcon(icon)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec()

#Запрашивает подтверждение
def confirm(parent, title: str, text: str) -> bool:
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Question)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return msg.exec() == QMessageBox.Ok
    
#Окно входа
###class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход в систему")
        self.setFixedSize(350, 250)
        self.session = get_session()
        self.init_ui()
    
    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(30, 20, 30, 20)

        QLabel("Магазин обуви").setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(QLabel("Магазин обуви"), alignment=Qt.AlignCenter)

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Логин")
        layout.addWidget(self.login_input)

        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Пароль")
        self.pass_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.pass_input)

        btn_layout = QHBoxLayout()

        btn_login = QPushButton("Войти")
        btn_login.clicked.connect(self.try_login)
        btn_layout.addWidget(btn_login)

        btn_guest = QPushButton("Гость")
        btn_guest.clicked.connect(self.enter_guest)
        btn_layout.addWidget(btn_guest)

        layout.addLayout(btn_layout)

        self.status = QLabel()
        self.status.setStyleSheet("color: red;")
        layout.addWidget(self.status, alignment=Qt.AlignCenter)

    def try_login(self):
        login = self.login_input.text().strip()
        pwd = self.pass_input.text()

        if not login or not pwd:
            self.status.setText("Введите логин и пароль")
            return
        
        user = self.session.query(User).filter(
            User.login == login, User.password == pwd
        ).first()

        if user:
            self.open_main(user)
        else:
            self.status.setText("Неверный логин или пароль")

    def enter_guest(self):
        guest = User(id=0, role=ROLE_GUEST, name="Гость", login="guest", password="", fio="Гость")
        self.open_main(guest)

    def open_main(self, user: User):
        self.main = MainWindow(user, self.session)
        self.main.show()
        self.close()
        
    def closeEvent(self, event):
        self.session.close()

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.session = get_session()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.user_role = None #Храним роль

        self.ui.loginBtn.clicked.connect(self.login)
        self.ui.guestBtn.clicked.connect(self.guest)
        
    def login(self):
        login = self.ui.loginInput.text().strip()
        password = self.ui.passInput.text()

        if not login:
            show_msg(self, "Ошибка", "Введите логин", QMessageBox.Warning)
            return
            
        if not password:
            show_msg(self, "Ошибка", "Введите пароль", QMessageBox.Warning) 
            return 

        user = self.session.query(User).filter(
            User.login == login, User.password == password
        ).first()
            
        if user:
            self.user_role = user.role
            self.accept() #Закрытие диалога
        else:
            show_msg(self, "Ошибка", "Неверный логин или пароль", QMessageBox.Critical)  
            return    
            
    def guest(self):
        self.user_role = ROLE_GUEST
        self.accept() #Закрытие диалога


class MainWindow(QMainWindow):
    logged_out = Signal() 
    def __init__(self, role: str):
        super().__init__()
        self.session = get_session()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.role = role

        # Отслеживание выбора
        self.selected_card = None
        self.selected_product = None

        self.setup_role_interface()
        self.setup_scroll_container() 
        self.load_products()

        self.ui.logoutBtn.clicked.connect(self.logout)

    def setup_role_interface(self):
        self.ui.searchInput.setVisible(False)
        self.ui.supplierLabel.setVisible(False)
        self.ui.suppliersCombo.setVisible(False)

        self.ui.editProductBtn.setVisible(False)
        self.ui.addProductBtn.setVisible(False)
        self.ui.deleteProductBtn.setVisible(False)

        #ИСПРАВИТЬ НА ФИО
        self.ui.fioUserLabel.setText(self.role)
        if self.role == ROLE_ADMIN:
            #ПОИСК
            self.ui.searchInput.setVisible(True)
            self.ui.searchInput.textChanged.connect(self.apply_filters)
            
            #Фильтр поставщика
            self.ui.suppliersCombo.setVisible(True)
            self.ui.suppliersCombo.addItem("Все поставщики")
            self.load_suppliers() #Загружаем и отображаем всех
            self.ui.suppliersCombo.currentTextChanged.connect(self.apply_filters)

            self.ui.supplierLabel.setVisible(True)
            
            #Кнопки
            self.ui.editProductBtn.setVisible(True)
            self.ui.editProductBtn.clicked.connect(self.edit_product)
            self.ui.addProductBtn.setVisible(True)
            self.ui.addProductBtn.clicked.connect(self.add_product)
            self.ui.deleteProductBtn.setVisible(True)
            self.ui.deleteProductBtn.clicked.connect(self.del_product)
        elif self.role == ROLE_MANAGER:
            self.ui.searchInput.setVisible(True)
            self.ui.supplierLabel.setVisible(True)
            self.ui.suppliersCombo.setVisible(True)

    def setup_scroll_container(self):
        self.cards_container = self.ui.scrollArea.widget()
        self.cards_layout = QVBoxLayout(self.cards_container)
       

    def load_products(self):
        products = self.session.query(Product).all()
        for product in products:
            self.add_single_card(product)
    
    def clear_product_cards(self):
        self.selected_card = None
        self.selected_product = None
        while self.cards_layout.count():
            item = self.cards_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    def load_suppliers(self):
        suppliers = self.session.query(Product.supplier).distinct().all()
        for s in suppliers:
            self.ui.suppliersCombo.addItem(s[0])
    
    def add_single_card(self, product):
        card_widget = QWidget()

        card_widget.product_data = product

        card_ui = Ui_ProductCard()
        card_ui.setupUi(card_widget)

        if product.image_url:
            pixmap = QPixmap(product.image_url)
        else:
            pixmap = QPixmap(PLACEHOLDER_IMAGE)

        pixmap = pixmap.scaled(300, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation);
        card_ui.label_photo.setPixmap(pixmap)

        card_ui.label_title.setText(f"{product.category} | {product.title}")
        card_ui.label_desc.setText(f"Описание: {product.description or 'Нет описания'}")
        card_ui.label_producer.setText(f"Производитель: {product.producer}")
        card_ui.label_supplier.setText(f"Поставщик: {product.supplier}")

        if(product.discount > 0):
            final = product.price * (100 - product.discount) / 100
            card_ui.label_price.setText(f"<font color='{COLOR_OLD_PRICE}'><s>{product.price:.2f}</s></font> {final:.2f} ₽")
        else:
            card_ui.label_price.setText(f"Цена: {product.price} ₽")

        card_ui.label_measure.setText(f"Единица измерения: {product.measure_type}")
        
        card_ui.label_count.setText(f"Кол-во: {str(product.quantity)}")
        if (product.quantity <= 0):
            card_widget.setStyleSheet(f"#ProductCard {{background-color: {COLOR_OUT_OF_STOCK}}}")
        
        card_ui.label_discount.setText(f"Скидка: {str(product.discount)}")
        if (product.discount > 15):
            card_ui.widget_discount.setStyleSheet(f"background-color: {COLOR_DISCOUNT}")

        self.cards_layout.addWidget(card_widget)

        def on_click(event):
            if event.button() == Qt.LeftButton:
                self.select_card(card_widget)
                event.accept()
        
        card_widget.mousePressEvent = on_click

    def select_card(self, card_widget):
        if self.selected_card:
            self.selected_card.setStyleSheet("background-color: none")
        self.selected_card = card_widget
        self.selected_product = getattr(card_widget, 'product_data')
        self.selected_card.setStyleSheet(f"#ProductCard {{background-color: {COLOR_SELECTED_CARD}}}")

    def apply_filters(self):
        search_text = self.ui.searchInput.text().lower()
        combo_supplier = self.ui.suppliersCombo.currentText()
        
        query = self.session.query(Product)

        if search_text:
            query = query.filter(Product.title.like(f"%{search_text}%"))

        if combo_supplier and combo_supplier not in ("", "Все поставщики"):
            query = query.filter(Product.supplier == combo_supplier)

        products = query.all()
        self.clear_product_cards()
        for p in products:
            self.add_single_card(p)

    def edit_product(self):
        if self.selected_product == None:
            show_msg(self, "Внимание", "Для редактирования товара выберите его в списке", QMessageBox.Warning)
            return
        
        form_product = ProductForm(self.selected_product)
        if form_product.exec() == QDialog.Accepted:
            self.clear_product_cards()
            self.load_products()
            return

    def del_product(self):
        if self.selected_product == None:
            show_msg(self, "Внимание", "Для удаления товара выберите его в списке", QMessageBox.Warning)
            return
        
        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            "Вы действительно хотите удалить товар",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.session.delete(self.selected_product)
                self.session.commit()

                self.selected_card = None
                self.selected_product = None
                
                self.apply_filters()

                show_msg(self, "Успех", "Товар успешно удален")
            except Exception as e:
                self.session.rollback()
                show_msg(self, "Ошибка", f"Произошла ошибка {e}", QMessageBox.Critical)
    
    def add_product(self):
        form_product = ProductForm(None)
        if form_product.exec() == QDialog.Accepted:
            self.clear_product_cards()
            self.load_products()
            return

    def logout(self):
        self.role = None
        self.session.close() 
        self.close()
        self.logged_out.emit()

class ProductForm(QDialog):
    def __init__(self, product: Product):
        super().__init__()
        self.session = get_session()
        self.product = product if product is not None else Product()
        self.ui = Ui_ProductForm()
        self.ui.setupUi(self)
        if product != None:
            self.set_product_data()
        self.set_combo_boxes()
        self.setupBtns()
        self.ui.add_photo_btn.clicked.connect(self.add_photo)

    def set_product_data(self):
        self.ui.articleProduct.setText(self.product.article)
        self.ui.nameProduct.setText(self.product.title)
        self.ui.descProduct.setText(f"Описание: {self.product.description or ''}")
        self.ui.supplierProduct.setText(self.product.supplier)
        self.ui.priceProduct.setText(str(self.product.price))
        self.ui.countProduct.setText(str(self.product.quantity))
        self.ui.discountProduct.setText(str(self.product.discount))
        
    def set_combo_boxes(self):
        categories = self.session.query(Product.category).distinct().all()
        producers = self.session.query(Product.producer).distinct().all()
        measure_types = self.session.query(Product.measure_type).distinct().all()  
        
        for c in categories:
            self.ui.comboCategory.addItem(str(c[0]))

        for p in producers:
            self.ui.comboProducer.addItem(str(p[0]))

        for mt in measure_types:
            self.ui.comboUnit.addItem(str(mt[0]))

    def setupBtns(self):
        self.ui.cancelBtn.clicked.connect(self.reject)
        self.ui.saveBtn.clicked.connect(self.save_product)

    def add_photo(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
            "./",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path:
            self.product.image_url = resize_image(file_path)


    def save_product(self):
        if not self.validate():
            return
        try:
            self.product.article = self.ui.articleProduct.text()
            self.product.title = self.ui.nameProduct.text().strip()
            self.product.supplier = self.ui.supplierProduct.text()
            self.product.price = float(self.ui.priceProduct.text())
            self.product.quantity = int(self.ui.countProduct.text())
            self.product.discount = float(self.ui.discountProduct.text())
            self.product.desc = self.ui.descProduct.text()
            self.product.category = self.ui.comboCategory.currentText()
            self.product.producer = self.ui.comboProducer.currentText()
            self.product.measure_type = self.ui.comboUnit.currentText()

            self.session.add(self.product)
            self.session.commit()
            self.accept()
        except Exception as e:
            self.session.rollback()
            show_msg(self, "Ошибка", f"Произошла ошибка {e}", QMessageBox.Critical)
            self.reject()

    def validate(self):
        article = self.ui.articleProduct.text()
        if not article:
            show_msg(self, "Ошибка", "Артикул не может быть пустым")
            return False
        
        name = self.ui.nameProduct.text().strip()
        if not name:
            show_msg(self, "Ошибка", "Название не может быть пустым")
            return False
        
        supplier = self.ui.supplierProduct.text()
        if not supplier:
            show_msg(self, "Ошибка", "Поставщик не может быть пустым")
            return False
        
        price = float(self.ui.priceProduct.text())
        if price <= 0:
            show_msg(self, "Ошибка", "Цена должна быть > 0")  
        try:
            count = int(self.ui.countProduct.text())
            if count < 0:
                show_msg(self, "Ошибка", "Кол-во не должно быть < 0")  
                return False
        except ValueError:
            show_msg(self, "Ошибка", "Неверный формат")
            return False

        discount = float(self.ui.discountProduct.text())
        if not (0 <= discount <= 100):
            show_msg(self, "Ошибка", "Скидка должна быть от 0 до 100")
            return False
        return True
    


def main():
    init_db()
    test_db_content()

    app = QApplication(sys.argv)
    while True:
        login_win = LoginWindow()
        if login_win.exec() != QDialog.Accepted:
            break

        role = login_win.user_role
        main_win = MainWindow(role)

        main_win.logged_out.connect(main_win.close)

        main_win.show() 
        app.exec()

if __name__ == "__main__":
    main()