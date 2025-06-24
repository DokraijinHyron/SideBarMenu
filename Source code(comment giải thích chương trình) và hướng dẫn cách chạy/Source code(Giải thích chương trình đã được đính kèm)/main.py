from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QMainWindow # Nhập các module cần thiết từ PyQt6.QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets  # Nhập các module cần thiết từ PyQt6
import sys  # Nhập module sys để sử dụng hệ thống
from project_ui_import import Ui_MainWindow  # Nhập lớp Ui_MainWindow từ project_ui_import

class MysideBar(QMainWindow, Ui_MainWindow):  # Định nghĩa lớp MysideBar kế thừa từ QMainWindow và Ui_MainWindow

    def setupUi(self, MainWindow):  # Định nghĩa phương thức setupUi để thiết lập giao diện chính
        super().setupUi(MainWindow)
        self.sidenum = 0  # Khởi tạo biến sidenum với giá trị ban đầu là 0
        self.icon_name_widget.setMaximumWidth(0)  # Đặt chiều rộng tối đa của icon_name_widget là 0
        self.stackedWidget.setCurrentWidget(self.dashboard_page)  # Đặt trang hiển thị hiện tại là dashboard_page
        self.stackedWidget.setCurrentWidget(self.profile_page)  # Đặt trang hiển thị hiện tại là profile_page
        self.stackedWidget.setCurrentWidget(self.timetable_page)  # Đặt trang hiển thị hiện tại là timetable_page
        self.stackedWidget.setCurrentWidget(self.marktable_page)  # Đặt trang hiển thị hiện tại là marktable_page
        self.dashboard_2.clicked.connect(lambda: self.switch_widget(1))  # Kết nối sự kiện clicked của dashboard_2 với phương thức switch_widget(1)
        self.profile_2.clicked.connect(lambda:self.switch_widget(2))  # Kết nối sự kiện clicked của profile_2 với phương thức switch_widget(2)
        self.timetable_2.clicked.connect(lambda:self.switch_widget(3))  # Kết nối sự kiện clicked của timetable_2 với phương thức switch_widget(3)
        self.marktable_2.clicked.connect(lambda:self.switch_widget(4))  # Kết nối sự kiện clicked của marktable_2 với phương thức switch_widget(4)
        self.register_2.clicked.connect(lambda:self.switch_widget(5))  # Kết nối sự kiện clicked của register_2 với phương thức switch_widget(5)
        self.payment_2.clicked.connect(lambda:self.switch_widget(6))  # Kết nối sự kiện clicked của payment_2 với phương thức switch_widget(6)
        self.support_2.clicked.connect(lambda:self.switch_widget(8))  # Kết nối sự kiện clicked của support_2 với phương thức switch_widget(8)
        self.video_2.clicked.connect(lambda:self.switch_widget(7))  # Kết nối sự kiện clicked của video_2 với phương thức switch_widget(7)
        self.dashboard_1.clicked.connect(lambda: self.switch_widget(1))  # Kết nối sự kiện clicked của dashboard_1 với phương thức switch_widget(1)
        self.profile_1.clicked.connect(lambda:self.switch_widget(2))  # Kết nối sự kiện clicked của profile_1 với phương thức switch_widget(2)
        self.timetable_1.clicked.connect(lambda:self.switch_widget(3))  # Kết nối sự kiện clicked của timetable_1 với phương thức switch_widget(3)
        self.marktable_1.clicked.connect(lambda:self.switch_widget(4))  # Kết nối sự kiện clicked của marktable_1 với phương thức switch_widget(4)
        self.register_1.clicked.connect(lambda:self.switch_widget(5))  # Kết nối sự kiện clicked của register_1 với phương thức switch_widget(5)
        self.payment_1.clicked.connect(lambda:self.switch_widget(6))  # Kết nối sự kiện clicked của payment_1 với phương thức switch_widget(6)
        self.support_1.clicked.connect(lambda:self.switch_widget(8))  # Kết nối sự kiện clicked của support_1 với phương thức switch_widget(8)
        self.video_1.clicked.connect(lambda:self.switch_widget(7))  # Kết nối sự kiện clicked của video_1 với phương thức switch_widget(7)
        self.okButton.clicked.connect(lambda:self.tinhtoan())  # Kết nối sự kiện clicked của okButton với phương thức tinhtoan()
        self.logout_2.clicked.connect(self.confirmExit)  # Kết nối sự kiện clicked của logout_2 với phương thức confirmExit()
        self.logout_1.clicked.connect(self.confirmExit)  # Kết nối sự kiện clicked của logout_1 với phương thức confirmExit()

    def maximum_menu(self):  # Định nghĩa phương thức maximum_menu để mở rộng hoặc thu nhỏ menu
        if self.sidenum == 0:  # Nếu sidenum bằng 0 thì mở rộng menu
            self.icon_only_widget.hide()  # Ẩn widget icon_only_widget
            self.animation1 = QtCore.QPropertyAnimation(self.icon_name_widget, b"minimumWidth")  # Tạo animation1 để thay đổi chiều rộng tối thiểu của icon_name_widget
            self.animation2 = QtCore.QPropertyAnimation(self.icon_name_widget, b"maximumWidth")  # Tạo animation2 để thay đổi chiều rộng tối đa của icon_name_widget
            self.animation1.setDuration(200)  # Đặt thời gian chạy của animation1 là 200ms
            self.animation2.setDuration(200)  # Đặt thời gian chạy của animation2 là 200ms
            self.animation1.setStartValue(0)  # Đặt giá trị bắt đầu của animation1 là 0
            self.animation2.setStartValue(0)  # Đặt giá trị bắt đầu của animation2 là 0
            self.animation1.setEndValue(150)  # Đặt giá trị kết thúc của animation1 là 150
            self.animation2.setEndValue(150)  # Đặt giá trị kết thúc của animation2 là 150
            self.animation1.setEasingCurve(QtCore.QEasingCurve.Type.OutCubic)  # Đặt đường cong gia tốc của animation1 là OutCubic
            self.animation2.setEasingCurve(QtCore.QEasingCurve.Type.OutCubic)  # Đặt đường cong gia tốc của animation2 là OutCubic
            self.animation1.start()  # Khởi chạy animation1
            self.animation2.start()  # Khởi chạy animation2
            def set_sidenum_to_1():
                self.sidenum = 1  # Thiết lập biến sidenum thành 1 khi animation1 kết thúc
            self.animation1.finished.connect(set_sidenum_to_1)  # Kết nối sự kiện finished của animation1 với hàm set_sidenum_to_1
        else:
            self.animation1 = QtCore.QPropertyAnimation(self.icon_name_widget, b"minimumWidth")  # Tạo animation1 để thay đổi chiều rộng tối thiểu của widget icon_name_widget
            self.animation2 = QtCore.QPropertyAnimation(self.icon_name_widget, b"maximumWidth")  # Tạo animation2 để thay đổi chiều rộng tối đa của widget icon_name_widget
            self.animation1.setDuration(200)  # Thiết lập thời gian chạy của animation1 là 200 milliseconds
            self.animation2.setDuration(200)  # Thiết lập thời gian chạy của animation2 là 200 milliseconds
            self.animation1.setStartValue(150)  # Thiết lập giá trị bắt đầu của animation1 là 150
            self.animation2.setStartValue(150)  # Thiết lập giá trị bắt đầu của animation2 là 150
            self.animation1.setEndValue(0)  # Thiết lập giá trị kết thúc của animation1 là 0
            self.animation2.setEndValue(0)  # Thiết lập giá trị kết thúc của animation2 là 0
            self.animation1.setEasingCurve(QtCore.QEasingCurve.Type.OutCubic)  # Thiết lập đường cong chuyển động của animation1 là OutCubic
            self.animation2.setEasingCurve(QtCore.QEasingCurve.Type.OutCubic)  # Thiết lập đường cong chuyển động của animation2 là OutCubic
            self.animation1.start()  # Khởi chạy animation1
            self.animation2.start()  # Khởi chạy animation2
            def set_sidenum_to_0():
                self.sidenum = 0  # Thiết lập biến sidenum thành 0 khi animation1 kết thúc
            self.animation1.finished.connect(set_sidenum_to_0)  # Kết nối sự kiện finished của animation1 với hàm set_sidenum_to_0
            self.animation1.finished.connect(self.icon_only_widget.show)  # Hiển thị widget icon_only_widget khi animation1 kết thúc

    def switch_widget(self, index):
        if index == 1:
            self.stackedWidget.setCurrentWidget(self.dashboard_page)  # Chuyển đến trang dashboard_page
        if index == 2:
            self.stackedWidget.setCurrentWidget(self.profile_page)  # Chuyển đến trang profile_page
        if index == 3:
            self.stackedWidget.setCurrentWidget(self.timetable_page)  # Chuyển đến trang timetable_page
        if index == 4:
            self.stackedWidget.setCurrentWidget(self.marktable_page)  # Chuyển đến trang marktable_page
        if index == 5:
            self.stackedWidget.setCurrentWidget(self.register_page)  # Chuyển đến trang register_page
        if index == 6:
            self.stackedWidget.setCurrentWidget(self.payment_page)  # Chuyển đến trang payment_page
        if index == 7:
            self.stackedWidget.setCurrentWidget(self.video_page)  # Chuyển đến trang video_page
        if index == 8:
            self.stackedWidget.setCurrentWidget(self.supporter_page)  # Chuyển đến trang supporter_page

    def confirmExit(self):
        msg_box = QMessageBox()  # Tạo một hộp thoại thông báo
        msg_box.setWindowTitle("Exit Confirmation")  # Thiết lập tiêu đề của hộp thoại
        msg_box.setText("Bạn có muốn thoát?")  # Thiết lập nội dung của hộp thoại
        yes_button = msg_box.addButton("Yes", QMessageBox.ButtonRole.AcceptRole)  # Thêm nút "Yes" vào hộp thoại
        no_button = msg_box.addButton("No", QMessageBox.ButtonRole.RejectRole)  # Thêm nút "No" vào hộp thoại
        msg_box.setDefaultButton(no_button)  # Thiết lập nút "No" là nút mặc định
        msg_box.exec()  # Hiển thị hộp thoại và chờ người dùng chọn
        if msg_box.clickedButton() == yes_button:
            QApplication.quit()  # Thoát khỏi ứng dụng nếu người dùng chọn "Yes"
    
    def tinhtoan(self):
        # Lấy giá trị từ các ô nhập liệu "Avalue" và "Bvalue"
        A = self.Avalue.text()
        B = self.Bvalue.text()
        
        # Tính tổng của A và B, chuyển kết quả về định dạng chuỗi và hiển thị trên ô "sum_line"
        self.sum_line.setText(f'{int(A) + int(B)} VND')
        
        # Hiển thị một hộp thoại thông báo tổng của A và B
        msg = QtWidgets.QMessageBox()
        msg.setInformativeText(f"Tong cong la {int(A) + int(B)} VND")
        msg.exec()

if __name__ == "__main__":
    # Khởi tạo ứng dụng Qt
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()  # Tạo một cửa sổ chính (QMainWindow)
    ui = MysideBar()  # Tạo một đối tượng "ui" của lớp MysideBar 
    ui.setupUi(MainWindow)  #Thiết lập giao diện cho cửa sổ chính 
    MainWindow.show()   # Hiển thị cửa sổ chính
    
    # Chạy vòng lặp sự kiện của ứng dụng Qt
    sys.exit(app.exec())