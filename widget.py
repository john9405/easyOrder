# This Python file uses the following encoding: utf-8
import base64
import binascii
import json
import os
import re
import sys
import tempfile

import requests
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from appstoreserverlibrary.api_client import AppStoreServerAPIClient, APIException
from appstoreserverlibrary.models.Environment import Environment

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Worker(QThread):
    callback = Signal(str)

    def __init__(self):
        super().__init__()
        self.private_key = None
        self.key_id = None
        self.issuer_id = None
        self.bundle_id = None
        self.environment = None
        self.order_id = None

    def set_value(self, **kwargs):
        self.private_key = kwargs.get('private_key')
        self.key_id = kwargs.get('key_id')
        self.issuer_id = kwargs.get('issuer_id')
        self.bundle_id = kwargs.get('bundle_id')
        self.environment = kwargs.get('environment')
        self.order_id = kwargs.get('order_id')

    def run(self):
        client = AppStoreServerAPIClient(self.private_key, self.key_id, self.issuer_id, self.bundle_id, self.environment)
        try:
            response = client.look_up_order_id(self.order_id)
            if response.status == 0:
                for signedTransaction in response.signedTransactions:
                    try:
                        temp = signedTransaction.split('.')[1]
                        temp = temp.replace('-', '+')
                        temp = temp.replace('_', '/')
                        while len(temp) % 4 != 0:
                            temp += '='
                        temp = base64.b64decode(temp)
                        print(temp)
                        self.callback.emit(json.dumps(json.loads(temp), ensure_ascii=False, indent=4))
                    except binascii.Error:
                        self.callback.emit(signedTransaction)
            else:
                self.callback.emit("OrderId is not valid!")
        except APIException as e:
            self.callback.emit(str(e))
        except requests.exceptions.ConnectionError:
            self.callback.emit("HTTPSConnectionPool")


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.sel_btn.clicked.connect(self.on_select)
        self.ui.sub_btn.clicked.connect(self.on_submit)
        self.ui.clr_btn.clicked.connect(self.on_clear)
        self.on_start()
        self.thread = Worker()
        self.thread.callback.connect(self.callback)

    def on_start(self):
        temp_dir = tempfile.gettempdir()
        filepath = os.path.join(temp_dir, 'eoconfig.json')
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                try:
                    data = json.loads(f.read())
                    self.ui.issuerId.setText(data.get('issuer_id', ''))
                    self.ui.keyId.setText(data.get('key_id', ''))
                    self.ui.bundleId.setText(data.get('bundle_id', ''))
                    self.ui.filePath.setText(data.get('file_path', '/path/to/SubscriptionKey_xxx.p8'))
                    self.ui.orderId.setText(data.get('order_id', ''))
                    if data.get('environment', '') == Environment.SANDBOX:
                        self.ui.SANDBOX.setChecked(True)
                except json.JSONDecodeError:
                    pass

    def on_select(self):
        file_dialog = QFileDialog()
        file_dialog.setDirectory("~")
        file_dialog.setNameFilter("KeyFile(*.p8)")
        if file_dialog.exec():
            if len(file_dialog.selectedFiles()) > 0:
                self.ui.filePath.setText(file_dialog.selectedFiles()[0])

    def on_submit(self):
        self.ui.textBrowser.setText('Searching...')

        file_path = self.ui.filePath.text()
        if not os.path.exists(file_path):
            QMessageBox.critical(self, "Error", "Please enter the correct certificate path!")
            return

        with open(file_path, "rb") as f:
            private_key = f.read()

        if self.ui.PRODUCTION.isChecked():
            environment = Environment.PRODUCTION
        elif self.ui.SANDBOX.isChecked():
            environment = Environment.SANDBOX

        pattern = re.compile(r'^[A-Za-z0-9\-\.]+$')
        issuer_id = self.ui.issuerId.text()
        if pattern.search(issuer_id) is None:
            QMessageBox.critical(self, "Error", "Please enter a issuer id!")
            return

        bundle_id = self.ui.bundleId.text()
        if pattern.search(bundle_id) is None:
            QMessageBox.critical(self, "Error", "Please enter a bundle id!")
            return

        key_id = self.ui.keyId.text()
        if pattern.search(key_id) is None:
            QMessageBox.critical(self, "Error", "Please enter a key id!")
            return

        order_id = self.ui.orderId.text()
        if pattern.search(order_id) is None:
            QMessageBox.critical(self, "Error", "Please enter an order id!")
            return

        temp_dir = tempfile.gettempdir()
        filepath = os.path.join(temp_dir, 'eoconfig.json')
        with open(filepath, 'w') as f:
            f.write(json.dumps({
                'issuer_id': issuer_id,
                'key_id': key_id,
                'bundle_id': bundle_id,
                'order_id': order_id,
                'environment': environment,
                'file_path': file_path
            }))

        self.thread.set_value(
            private_key=private_key,
            key_id=key_id,
            issuer_id=issuer_id,
            bundle_id=bundle_id,
            environment=environment,
            order_id=order_id
        )
        self.thread.start()

    def callback(self, text):
        self.ui.textBrowser.setText(text)

    def on_clear(self):
        self.ui.textBrowser.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
