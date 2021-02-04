import csv

class Contacto:
	def __init__(self, name, number, correo):
		self._nombre= name
		self._numero= number
		self._email = correo

	def make_new(self):
		new_cnt = [self._nombre, self._numero, self._email]
		return new_cnt

class ContactBook:
	def __init__(self):
		self.contactos=[]

	def agregar(self, nombre,numero,email):
		n_contact = Contacto(nombre, numero, email)
		self.contactos.append(n_contact.make_new())
		self.save()
		print('*El contacto ha sido agregado exitosamente...\n')

	def actualizar(self):
		name = str(input('Que contacto desea actualizar?: '))
		for cnt in self.contactos:
			if name in cnt:
				seccion = str(input('Que aspecto desea actualizar? \n*a)nombre\n*b)numero\n*c)email\n...Opcion: '))
				if seccion == 'a':
					new_name = str(input('Cual es el nuevo nombre?: '))
					cnt[0] = new_name
					print('*NOMBRE ACTUALIZADO')
				elif seccion == 'b':
					new_num = str(input('Cual es el nuevo numero?: '))
					cnt[1] = new_num
					print('*NUMERO ACTUALIZADO')
				elif seccion == 'c':
					new_email = str(input('Cual es el nuevo email?: '))
					cnt[2] = new_email
					print('*E-MAIL ACTUALIZADO')
				else:
					print('***Comando no reconocido')
			else:
				print('**El contacto no existe en la agenda')

	def eliminar(self, idx):
		for cnt in self.contactos:
			i=0
			if idx in cnt:
				self.contactos.pop(i)
				print('*El contacto {} ha sido eliminado...\n'.format(idx))
				self.save()
				break
			i+=1

	def display_cnt(self, name):
		for cnt in self.contactos:
			if name in cnt:
				print('''
				------------------------------------
				                  {}
				------------------------------------
				Número: {}
				E-mail: {}
				'''.format(cnt[0], cnt[1], cnt[2]))
			else:
				print('***No existe el contacto')

	def displaybook(self):
		for cnt in self.contactos:
			print('''
				------------------------------------
				                  {}
				------------------------------------
				Número: {}
				E-mail: {}
				'''.format(cnt[0], cnt[1], cnt[2]))

	def save(self):
		with open('contactos.csv','w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(('name','phone','email'))

			for contact in self.contactos:
				writer.writerow( (contact[0],contact[1],contact[2]) )


def main():
	libreta_de_contactos = ContactBook()

	#Agregar la ruta en donde se encuentra el archivo CSV
	with open('contactos.csv','r') as f:
		reader = csv.reader(f)
		for idx, row in enumerate(reader):
			if idx == 0:
				continue
			'''
			Era necesario agregar un if row=[] porque 
			se agragaba un salto de linea a cada dato nuevo si
			en with open('contactos.csv','w', newline='') no se 
			hubiera agregado el comando NEWLINE
			'''
			
			libreta_de_contactos.agregar(row[0],row[1],row[2])


	while True:
		print('Que accion desea realizar?')
		print('*a) buscar contacto')
		print('*b) actualizar contacto')
		print('*c) agregar contacto')
		print('*d) eliminar contacto')
		print('*e) imprimir lista de contactos')
		print('*s) salir')

		comando = str(input('Selecciona una opcion: '))

		if comando == 'a':
			name = str(input('Cual es el nombre del contacto?'))
			libreta_de_contactos.display_cnt(name)

		elif comando == 'b':
			libreta_de_contactos.actualizar()

		elif comando == 'c':
			name = str(input('Cual es el nombre del nuevo contacto?: '))
			num = str(input('Cual es el numero?: '))
			email = str(input('Cual es el email: '))

			libreta_de_contactos.agregar(name,num,email)

		elif comando == 'd':
			name = str(input('Cual es el nombre del contacto que desea eliminar?'))
			libreta_de_contactos.eliminar(name)

		elif comando == 'e':
			libreta_de_contactos.displaybook()

		elif comando == 's':
			break

		else:
			print('***No se reconoce el comando')

if __name__=='__main__':

	print('BIENVENIDO A TU AGENDA')

	main()