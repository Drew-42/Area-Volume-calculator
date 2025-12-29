import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
                             QHBoxLayout, QGridLayout, QLineEdit, QMainWindow, QComboBox)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

sys.path.append(os.path.abspath('program_files'))
import program_data

class Area_app(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Area & Volume Calculator App')
		self.move(300, 100)
		self.setMinimumWidth(590)
		self.setWindowIcon(QIcon('program_files/icon.png'))

		self.central_widget = QWidget()
		self.setCentralWidget(self.central_widget)

		self.initUI()

	def initUI(self):
		self.label1 = QLabel('Calculate AREA/VOLUME of:')
		self.label2 = QLabel('                             Length: ')
		self.label3 = QLabel('                    Unit: ')
		self.label4 = QLabel('                             Width: ')
		self.label5 = QLabel('                    Unit: ')
		self.label6 = QLabel('                             Height of shape: ')
		self.label7 = QLabel('                    Unit: ')
		self.label8 = QLabel('                             1ˢᵗ Semi-axis: ')
		self.label9 = QLabel('                    Unit: ')
		self.label10 = QLabel('                             2ⁿᵈ Semi-axis: ')
		self.label11 = QLabel('                    Unit: ')
		self.label12 = QLabel('                             3ʳᵈ Semi-axis: ')
		self.label13 = QLabel('                    Unit: ')
		self.label14 = QLabel('                             1ˢᵗ Base: ')
		self.label15 = QLabel('                    Unit: ')
		self.label16 = QLabel('                             2ⁿᵈ Base: ')
		self.label17 = QLabel('                    Unit: ')
		self.label18 = QLabel('                             Base of triangle: ')
		self.label19 = QLabel('                    Unit: ')
		self.label20 = QLabel(' Unit for RESULT: ')
		self.label21 = QLabel('Base: ')
		self.label22 = QLabel('                             Height of form: ')
		self.label23 = QLabel('                    Unit: ')
		self.label24 = QLabel('\nResult: ')

		self.line_edit1 = QLineEdit(self)
		self.line_edit2 = QLineEdit(self)
		self.line_edit3 = QLineEdit(self)
		self.line_edit4 = QLineEdit(self)
		self.line_edit5 = QLineEdit(self)
		self.line_edit6 = QLineEdit(self)
		self.line_edit7 = QLineEdit(self)
		self.line_edit8 = QLineEdit(self)
		self.line_edit9 = QLineEdit(self)
		self.line_edit10 = QLineEdit(self)

		self.picture = QLabel('')

		self.button1 = QPushButton('Calculate', self)
		self.button1.setFixedSize(100, 25)

		self.combo1 = QComboBox(self)
		self.combo1.addItems(['Choose shape/form', 'Rectangle/Square (A)', 'Triangle (A)', 
							  'Ellipse/Circle (A)', 'Trapezoid (A)', 'Pentagon (A)', 
							  'Hexagon (A)', 'Cuboid/Cube (V)', 'Ellipsoid/Sphere (V)', 
							  'Cylinder (V)', 'Pyramid/Cone (V)'])
		self.combo2 = QComboBox(self)
		self.combo2.addItems(['Choose base of pyramid/cone', 'Rectangle/Square', 'Triangle', 
							  'Ellipse/Circle', 'Trapezoid', 'Pentagon', 'Hexagon'])

		self.combo_unititems = ['Choose unit', 'qm (quectometers)', 'rm (rontometers)', 
						   'ym (yoctometers)', 'zm (zeptometers)', 'am (attometers)', 
						   'fm (femtometers)', 'pm (picometers)', 'nm (nanometers)', 
						   'μm (micrometers)', 'mm (millimeters)', 'cm (centimeters)', 
						   'dm (decimeters)', 'm (meters)', 'dam (decameters)', 
						   'hm (hectometers)', 'km (kilometers)', 'Mm (megameters)', 
						   'Gm (gigameters)', 'Tm (terameters)', 'Pm (petameters)', 
						   'Em (exameters)', 'Zm (zettameters)', 'Ym (yottameters)', 
						   'Rm (ronnameters)', 'Qm (quettameters)']

		self.combo_unit1 = QComboBox(self)
		self.combo_unit1.addItems(self.combo_unititems)
		self.combo_unit1.setFixedSize(130, 25)

		self.combo_unit2 = QComboBox(self)
		self.combo_unit2.addItems(self.combo_unititems)
		self.combo_unit2.setFixedSize(130, 25)

		self.combo_unit3 = QComboBox(self)
		self.combo_unit3.addItems(self.combo_unititems)
		self.combo_unit3.setFixedSize(130, 25)

		self.combo_unit4 = QComboBox(self)
		self.combo_unit4.addItems(self.combo_unititems)
		self.combo_unit4.setFixedSize(130, 25)

		self.combo_unit5 = QComboBox(self)
		self.combo_unit5.addItems(self.combo_unititems)
		self.combo_unit5.setFixedSize(130, 25)

		self.combo_unit6 = QComboBox(self)
		self.combo_unit6.addItems(self.combo_unititems)
		self.combo_unit6.setFixedSize(130, 25)

		self.combo_unit7 = QComboBox(self)
		self.combo_unit7.addItems(self.combo_unititems)
		self.combo_unit7.setFixedSize(130, 25)

		self.combo_unit8 = QComboBox(self)
		self.combo_unit8.addItems(self.combo_unititems)
		self.combo_unit8.setFixedSize(130, 25)

		self.combo_unit9 = QComboBox(self)
		self.combo_unit9.addItems(self.combo_unititems)
		self.combo_unit9.setFixedSize(130, 25)

		self.combo_unit10 = QComboBox(self)
		self.combo_unit10.addItems(self.combo_unititems)
		self.combo_unit10.setFixedSize(130, 25)

		self.combo_unit11 = QComboBox(self)
		self.combo_unit11.addItems(self.combo_unititems)
		self.combo_unit11.setFixedSize(130, 25)

		space = QLabel('')
		space.setFixedSize(50, 10)

		main_grid = self.central_widget.layout()
		if main_grid is None:
			main_grid = QGridLayout(self.central_widget)

		main_grid.addWidget(space, 0, 0)
		main_grid.addWidget(self.label1, 1, 0)
		main_grid.addWidget(self.combo1, 2, 0)
		main_grid.addWidget(space, 2, 1, 1, 4)
		main_grid.addWidget(self.button1, 2, 5)
		main_grid.addWidget(space, 3, 0)


		main_grid.addWidget(space, 4, 0)
		main_grid.addWidget(space, 5, 0)

		main_grid.addWidget(self.label21, 6, 0)
		main_grid.addWidget(self.combo2, 7, 0)
		
		main_grid.addWidget(self.label2, 8, 0)
		main_grid.addWidget(self.line_edit1, 8, 1)
		
		main_grid.addWidget(self.label3, 8, 2)
		main_grid.addWidget(self.combo_unit1, 8, 3)
		
		main_grid.addWidget(self.label4, 9, 0)
		main_grid.addWidget(self.line_edit2, 9, 1)
		
		main_grid.addWidget(self.label5, 9, 2)
		main_grid.addWidget(self.combo_unit2, 9, 3)
		
		main_grid.addWidget(self.label6, 10, 0)
		main_grid.addWidget(self.line_edit3, 10, 1)
		
		main_grid.addWidget(self.label7, 10, 2)
		main_grid.addWidget(self.combo_unit3, 10, 3)
		
		main_grid.addWidget(self.label8, 11, 0)
		main_grid.addWidget(self.line_edit4, 11, 1)
		
		main_grid.addWidget(self.label9, 11, 2)
		main_grid.addWidget(self.combo_unit4, 11, 3)
		
		main_grid.addWidget(self.label10, 12, 0)
		main_grid.addWidget(self.line_edit5, 12, 1)
		
		main_grid.addWidget(self.label11, 12, 2)
		main_grid.addWidget(self.combo_unit5, 12, 3)
		
		main_grid.addWidget(self.label12, 13, 0)
		main_grid.addWidget(self.line_edit6, 13, 1)
		
		main_grid.addWidget(self.label13, 13, 2)
		main_grid.addWidget(self.combo_unit6, 13, 3)
		
		main_grid.addWidget(self.label14, 14, 0)
		main_grid.addWidget(self.line_edit7, 14, 1)
		
		main_grid.addWidget(self.label15, 14, 2)
		main_grid.addWidget(self.combo_unit7, 14, 3)

		main_grid.addWidget(self.label16, 15, 0)
		main_grid.addWidget(self.line_edit8, 15, 1)
		
		main_grid.addWidget(self.label17, 15, 2)
		main_grid.addWidget(self.combo_unit8, 15, 3)
		
		main_grid.addWidget(self.label18, 16, 0)
		main_grid.addWidget(self.line_edit9, 16, 1)
		
		main_grid.addWidget(self.label19, 16, 2)
		main_grid.addWidget(self.combo_unit9, 16, 3)

		main_grid.addWidget(self.label22, 17, 0)
		main_grid.addWidget(self.line_edit10, 17, 1)

		main_grid.addWidget(self.label23, 17, 2)
		main_grid.addWidget(self.combo_unit10, 17, 3)

		main_grid.addWidget(self.label20, 18, 2)
		main_grid.addWidget(self.combo_unit11, 18, 3)

		main_grid.addWidget(self.label24, 19, 0, 1, 6)

		main_grid.addWidget(self.picture, 8, 5)


		self.label24.setStyleSheet('font-size: 20px; font-weight: bold;')


		self.reset_labels()


		self.combo1.currentTextChanged.connect(self.choice)
		self.combo2.currentTextChanged.connect(self.choice_conebase)
		self.button1.clicked.connect(self.calculate_clicked)

	def choice(self):
		if self.combo1.currentText() != 'Choose shape/form':
			self.reset_labels()
			self.clear_all_line_edits()
			self.reset_combos()
			self.combo2.setCurrentIndex(0)
			
			if self.combo1.currentText() == 'Rectangle/Square (A)': self.rectangle()

			if self.combo1.currentText() == 'Triangle (A)': self.triangle()

			if self.combo1.currentText() == 'Ellipse/Circle (A)': self.ellipse()

			if self.combo1.currentText() == 'Trapezoid (A)': self.trapezoid()

			if self.combo1.currentText() == 'Pentagon (A)': self.pentagon()

			if self.combo1.currentText() == 'Hexagon (A)': self.hexagon()

			if self.combo1.currentText() == 'Cuboid/Cube (V)': self.cuboid()

			if self.combo1.currentText() == 'Ellipsoid/Sphere (V)': self.ellipsoid()

			if self.combo1.currentText() == 'Cylinder (V)': self.cylinder()

			if self.combo1.currentText() == 'Pyramid/Cone (V)': self.pyramid()

	def rectangle(self):
		tuple_rectangle = (self.label2, self.label3, self.label4, self.label5, 
						   self.label20, self.line_edit1, self.line_edit2, self.picture, 
						   self.combo_unit1, self.combo_unit2, self.combo_unit11)
		for x in tuple_rectangle: x.setVisible(True)

	def triangle(self):
		tuple_triangle = (self.label6, self.label7, self.label18, self.label19, 
						  self.label20, self.line_edit3, self.line_edit9, self.picture, 
						  self.combo_unit3, self.combo_unit9, self.combo_unit11)
		for x in tuple_triangle: x.setVisible(True)

	def ellipse(self):
		tuple_circle = (self.label8, self.label9, self.label10, self.label11, 
						self.label20, self.line_edit4, self.line_edit5, self.picture, 
						self.combo_unit4, self.combo_unit5, self.combo_unit11)
		for x in tuple_circle: x.setVisible(True)

	def trapezoid(self):
		tuple_trapezoid = (self.label6, self.label7, self.label14, self.label15, 
						   self.label16, self.label17, self.label20, self.line_edit3, 
						   self.line_edit7, self.line_edit8, self.picture, self.combo_unit3, 
						   self.combo_unit7, self.combo_unit8, self.combo_unit11)
		for x in tuple_trapezoid: x.setVisible(True)

	def pentagon(self):
		tuple_pentagon = (self.label2, self.label3, self.label20, self.line_edit1, 
						  self.picture, self.combo_unit1, self.combo_unit11)
		for x in tuple_pentagon: x.setVisible(True)

	def hexagon(self):
		tuple_hexagon = (self.label2, self.label3, self.line_edit1, self.label20, 
						 self.picture, self.combo_unit1, self.combo_unit11)
		for x in tuple_hexagon: x.setVisible(True)

	def cuboid(self):
		tuple_cuboid = (self.label2, self.label3, self.label4, self.label5, self.label22, 
						self.label23, self.line_edit1, self.line_edit2, self.line_edit10, 
						self.label20, self.picture, self.combo_unit1, self.combo_unit2, 
						self.combo_unit10, self.combo_unit11)
		for x in tuple_cuboid: x.setVisible(True)

	def ellipsoid(self):
		tuple_ellipsoid = (self.label8, self.label9, self.label10, self.label11, 
						   self.label12, self.label13, self.line_edit4, self.line_edit5, 
						   self.line_edit6, self.label20, self.picture, self.combo_unit4, 
						   self.combo_unit5, self.combo_unit6, self.combo_unit11)
		for x in tuple_ellipsoid: x.setVisible(True)

	def cylinder(self):
		tuple_cylinder = (self.label8, self.label9, self.label10, self.label11, 
						  self.label22, self.label23, self.line_edit4, self.line_edit5, 
						  self.line_edit10, self.label20, self.picture, self.combo_unit4, 
						  self.combo_unit5, self.combo_unit10, self.combo_unit11)
		for x in tuple_cylinder: x.setVisible(True)

	def pyramid(self):
		tuple_pyramid = (self.label22, self.label23, self.line_edit10, self.label20, 
						 self.label21, self.combo2, self.picture, self.combo_unit10, 
						 self.combo_unit11)
		for x in tuple_pyramid: x.setVisible(True)

	def choice_conebase(self):
		if self.combo2.currentText() != 'Choose base of pyramid/cone':
			self.reset_labels_conebase()
			self.clear_all_line_edits()
			self.reset_combos()

			if self.combo2.currentText() == 'Rectangle/Square': self.rectangle()

			if self.combo2.currentText() == 'Triangle': self.triangle()

			if self.combo2.currentText() == 'Ellipse/Circle': self.ellipse()

			if self.combo2.currentText() == 'Trapezoid': self.trapezoid()

			if self.combo2.currentText() == 'Pentagon': self.pentagon()

			if self.combo2.currentText() == 'Hexagon': self.hexagon()

	def calculate_clicked(self):
		self.label24.setText('\nResult: ')
		try: 
			if self.combo1.currentText() == 'Rectangle/Square (A)': result, power_unit_result = self.calc_rectangle(), '²'
			if self.combo1.currentText() == 'Triangle (A)': result, power_unit_result = self.calc_triangle(), '²'
			if self.combo1.currentText() == 'Ellipse/Circle (A)': result, power_unit_result = self.calc_ellipse(), '²'
			if self.combo1.currentText() == 'Trapezoid (A)': result, power_unit_result = self.calc_trapezoid(), '²'
			if self.combo1.currentText() == 'Pentagon (A)': result, power_unit_result = self.calc_pentagon(), '²'
			if self.combo1.currentText() == 'Hexagon (A)': result, power_unit_result = self.calc_hexagon(), '²'
			if self.combo1.currentText() == 'Cuboid/Cube (V)': result, power_unit_result = self.calc_cuboid(), '³'
			if self.combo1.currentText() == 'Ellipsoid/Sphere (V)': result, power_unit_result = self.calc_ellipsoid(), '³'
			if self.combo1.currentText() == 'Cylinder (V)': result, power_unit_result = self.calc_cylinder(), '³'
			if self.combo1.currentText() == 'Pyramid/Cone (V)': result, power_unit_result = self.calc_pyramid(), '³'

			unit_result = self.units(self.combo_unit11.currentText())

			self.label24.setText(self.label24.text() + f'{result} {unit_result}{power_unit_result}')

		except Exception:
			self.label24.setText('\nError: Check your inputs (or lack thereof)!')

		self.label24.setVisible(True)

	def calc_rectangle(self):
		length = float(self.line_edit1.text())
		unit_length = self.units(self.combo_unit1.currentText())

		width = float(self.line_edit2.text())
		unit_width = self.units(self.combo_unit2.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.area_rectangle(length, width, unit_length, unit_width, unit_final)

	def calc_triangle(self):
		base = float(self.line_edit9.text())
		unit_base = self.units(self.combo_unit9.currentText())

		height = float(self.line_edit3.text())
		unit_height = self.units(self.combo_unit3.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.area_triangle(base, height, unit_base, unit_height, unit_final)

	def calc_ellipse(self):
		radius1 = float(self.line_edit4.text())
		unit_radius1 = self.units(self.combo_unit4.currentText())

		radius2 = float(self.line_edit5.text())
		unit_radius2 = self.units(self.combo_unit5.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.area_ellipse(radius1, radius2, unit_radius1, unit_radius2, unit_final)

	def calc_trapezoid(self):
		base1 = float(self.line_edit7.text())
		unit_base1 = self.units(self.combo_unit7.currentText())

		base2 = float(self.line_edit8.text())
		unit_base2 = self.units(self.combo_unit8.currentText())

		height = float(self.line_edit3.text())
		unit_height = self.units(self.combo_unit3.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.area_trapezoid(base1, base2, height, unit_base1, unit_base2, unit_height, unit_final)

	def calc_pentagon(self):
		length = float(self.line_edit1.text())
		unit_length = self.units(self.combo_unit1.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.area_pentagon(length, unit_length, unit_final)

	def calc_hexagon(self):
		length = float(self.line_edit1.text())
		unit_length = self.units(self.combo_unit1.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.area_hexagon(length, unit_length, unit_final)

	def calc_cuboid(self):
		length = float(self.line_edit1.text())
		unit_length = self.units(self.combo_unit1.currentText())

		width = float(self.line_edit2.text())
		unit_width = self.units(self.combo_unit2.currentText())
		
		height_form = float(self.line_edit10.text())
		unit_height_form = self.units(self.combo_unit10.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.volume_cuboid(length, width, height_form, unit_length, unit_width, unit_height_form, unit_final)

	def calc_ellipsoid(self):
		radius1 = float(self.line_edit4.text())
		unit_radius1 = self.units(self.combo_unit4.currentText())

		radius2 = float(self.line_edit5.text())
		unit_radius2 = self.units(self.combo_unit5.currentText())

		radius3 = float(self.line_edit6.text())
		unit_radius3 = self.units(self.combo_unit6.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.volume_ellipsoid(radius1, radius2, radius3, unit_radius1, unit_radius2, unit_radius3, unit_final)

	def calc_cylinder(self):
		radius1 = float(self.line_edit4.text())
		unit_radius1 = self.units(self.combo_unit4.currentText())

		radius2 = float(self.line_edit5.text())
		unit_radius2 = self.units(self.combo_unit5.currentText())

		height_form = float(self.line_edit10.text())
		unit_height_form = self.units(self.combo_unit10.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.volume_cylinder(radius1, radius2, height_form, unit_radius1, unit_radius2, unit_height_form, unit_final)

	def calc_pyramid(self):
		if self.combo2.currentText() == 'Rectangle/Square': pyr_base = self.calc_rectangle()

		if self.combo2.currentText() == 'Triangle': pyr_base = self.calc_triangle()

		if self.combo2.currentText() == 'Ellipse/Circle': pyr_base = self.calc_ellipse()

		if self.combo2.currentText() == 'Trapezoid': pyr_base = self.calc_trapezoid()

		if self.combo2.currentText() == 'Pentagon': pyr_base = self.calc_pentagon()

		if self.combo2.currentText() == 'Hexagon': pyr_base = self.calc_hexagon()

		height_form = float(self.line_edit10.text())
		unit_height_form = self.units(self.combo_unit10.currentText())

		unit_final = self.units(self.combo_unit11.currentText())

		return program_data.volume_pyramid(pyr_base, height_form, unit_final, unit_height_form, unit_final)

	def units(self, unit_input):
		if unit_input == self.combo_unititems[1]: return 'qm'
		if unit_input == self.combo_unititems[2]: return 'rm'
		if unit_input == self.combo_unititems[3]: return 'ym'
		if unit_input == self.combo_unititems[4]: return 'zm'
		if unit_input == self.combo_unititems[5]: return 'am'
		if unit_input == self.combo_unititems[6]: return 'fm'
		if unit_input == self.combo_unititems[7]: return 'pm'
		if unit_input == self.combo_unititems[8]: return 'nm'
		if unit_input == self.combo_unititems[9]: return 'μm'
		if unit_input == self.combo_unititems[10]: return 'mm'
		if unit_input == self.combo_unititems[11]: return 'cm'
		if unit_input == self.combo_unititems[12]: return 'dm'
		if unit_input == self.combo_unititems[13]: return 'm'
		if unit_input == self.combo_unititems[14]: return 'dam'
		if unit_input == self.combo_unititems[15]: return 'hm'
		if unit_input == self.combo_unititems[16]: return 'km'
		if unit_input == self.combo_unititems[17]: return 'Mm'
		if unit_input == self.combo_unititems[18]: return 'Gm'
		if unit_input == self.combo_unititems[19]: return 'Tm'
		if unit_input == self.combo_unititems[20]: return 'Pm'
		if unit_input == self.combo_unititems[21]: return 'Em'
		if unit_input == self.combo_unititems[22]: return 'Zm'
		if unit_input == self.combo_unititems[23]: return 'Ym'
		if unit_input == self.combo_unititems[24]: return 'Rm'
		if unit_input == self.combo_unititems[25]: return 'Qm'

	def reset_labels(self):
		tuple_labels = (self.label2, self.label3, self.label4, self.label5, self.label6, 
						self.label7, self.label8, self.label9, self.label10, self.label11, 
						self.label12, self.label13, self.label14, self.label15, 
						self.label16, self.label17, self.label18, self.label19, 
						self.label20, self.label21, self.label22, self.label23, self.label24, 
						self.combo2, self.line_edit1, self.line_edit2, self.line_edit3, 
						self.line_edit4, self.line_edit5, self.line_edit6, self.line_edit7, 
						self.line_edit8, self.line_edit9, self.line_edit10, self.picture, 
						self.combo_unit1, self.combo_unit2, self.combo_unit3, 
						self.combo_unit4, self.combo_unit5, self.combo_unit6, 
						self.combo_unit7, self.combo_unit8, self.combo_unit9, 
						self.combo_unit10, self.combo_unit11)
		for x in tuple_labels: x.setVisible(False)

	def reset_labels_conebase(self):
		tuple_labels_conebase = (self.label2, self.label3, self.label4, self.label5, 
								 self.label6, self.label7, self.label8, self.label9, 
								 self.label10, self.label11, self.label12, self.label13, 
								 self.label14, self.label15, self.label16, self.label17, 
								 self.label18, self.label19, self.label20, self.label24, 
								 self.line_edit1, self.line_edit2, self.line_edit3, 
								 self.line_edit4, self.line_edit5, self.line_edit6, 
								 self.line_edit7, self.line_edit8, self.line_edit9, 
								 self.picture, self.combo_unit1, self.combo_unit2, 
								 self.combo_unit3, self.combo_unit4, self.combo_unit5, 
								 self.combo_unit6, self.combo_unit7, self.combo_unit8, 
								 self.combo_unit9, self.combo_unit11)
		for x in tuple_labels_conebase: x.setVisible(False)

	def clear_all_line_edits(self):
		for line_edit in (self.line_edit1, self.line_edit2, self.line_edit3, self.line_edit4, 
						  self.line_edit5, self.line_edit6, self.line_edit7, self.line_edit8, 
						  self.line_edit9, self.line_edit10):
			line_edit.clear()

	def reset_combos(self):
		for combo in (self.combo_unit1, self.combo_unit2, self.combo_unit3, self.combo_unit4, 
					  self.combo_unit5, self.combo_unit6, self.combo_unit7, self.combo_unit8, 
					  self.combo_unit9, self.combo_unit10, self.combo_unit11):
			combo.setCurrentIndex(0)

def main():
	app = QApplication(sys.argv)
	area_app = Area_app()
	area_app.show()
	sys.exit(app.exec())

if __name__ == '__main__':
	main()