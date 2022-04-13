def imt(self):
    weight = int(self.textEdit_weight.text())
    height = int(self.textEdit_height.text())
    imt_result = weight / (height / 100) ** 2
    return float(f'{imt_result:.1f}')

