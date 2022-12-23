from docxtpl import DocxTemplate
doc = DocxTemplate("INSURANCE ILLINOIS 2.docx")
name = input('name: ')
car = input('car: ')
viin = input('vin: ')
context = { 'name' : name, 'car' : car, 'viin': viin}
doc.render(context)
doc.save("шаблон-final.docx")