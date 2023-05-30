'''
Juan Miguel Rojas Noriega 2227517
'''



import os #Libreria Os para reiniciar pantalla.
from datetime import datetime #Libreria para llamar fechas y horas actuales para la facturación.

dicc_user={'1143873302':['1143873302','A','JUAN MIGUEL ROJAS','3246523']} #Diccionario de Usuarios
inv_inicial={'1':['1','Pantalon',150,25000],'2':['2','Camisas',100,10000],'3':['3','Sacos',5,45000],'4':['4','Sombrero',10,5000],'5':['5','Zapato Dep',11,90000],'6':['6','Zapato For',11,90000]} #Diccionarios de Inventario
lista_compras={} #Diccionario de la lista de compras
lista_descuento={} #Diccionario que guarda los descuentos otorgados
ganancias=[] #Lista que guarda las ganancias de cada factura hecha
def mostrar_inventario():
  print("El Inventario Actual es:\n")
  print("Referencia     Descripción    Cantidad   Valor Total")
  for i in inv_inicial:
    print(f'{inv_inicial[i][0]:17}{inv_inicial[i][1]:10}{inv_inicial[i][2]:8}{"":8}{"${:.0f}".format(inv_inicial[i][3]):10}')  #Imprime el inventario actual, para llevar un control, esto lo hace con un format que alinea todo por columnas dependiendo de unas unidades especificas, (:17,:10,:8,:8)

def mostrar_compras():
  print("Su lista de Compras Actual es:\n") #Imprime la lista de compras actual
  print("Referencia     Descripción    Cantidad   Valor Total")
  for i in lista_compras:
      print(f'{lista_compras[i][0]:17}{lista_compras[i][1]:10}{lista_compras[i][2]:8}{"":8}{"${:.0f}".format(lista_compras[i][3]):10}')

def config_inicial(): #Función principal del código
  


  #----------------------------------------MENÚ Y REGISTROS-------------------------------------

  
  while True: #Menú Principal
    print("=================BIENVENIDOS A AJASITOSNO=================\n")
    print("----------------------MENÚ PRINCIPAL----------------------")
    print("1.Crear un Usuario")
    print("2.Ingresar al Menú de Admin ")
    print("3.Ingresar al Menú de Vendedor")
    print("4.Salir del Programa\n")
    
    menu=input("Ingrese una Opcion: ")#Opcion de menu principal
    os.system('clear')

    if menu=="1": #Crear Usuario Admin o Vendedor
      print("=======================REGÍSTRATE=======================\n")
      ID=input ("Ingrese Identificación: ")#Ingresar la Id a registrar
      while True:
        tipo=input("Ingrese tipo de usuario (A/V): ")#ingresar los tipos de usuario (admin o vendedor)
        if tipo=="a" or tipo=="A" or tipo=="v" or tipo=="V":#El while verifica que solo pueda ingresarse estos datos
          break         
        else:
          print("Ingrese datos válidos")
      while True:
        password=input("Ingrese una contraseña: ")#ingresar la contraseña que será del usuario
        password1=input("Confirme su Contraseña: ")#confirmar contraseña
        if password!=password1:
          print("Las contraseñas no coinciden")    #Condicional para que la contraseña y la confirmacion coincidan
        elif password==password1:
          break
        else:
          print("Ingrese datos válidos")
      nombre=input("Ingrese sus Nombres y Apellidos: ")     #Ingresa el nombre del Usuario a crear
      dicc_user[ID]=[ID,tipo,nombre,password]  #Agrega todos los datos ingresados a un diccionario de Usuarios
      os.system('clear')
      print("=====Usted Ha Sido Registrado con Éxito=====\n")

      
#---------------------------------------------------------FUNCIONES DE ADMIN--------------------------------------------------

      
    elif menu=="2": #Ingresar con un usuario existente que sea Admin.
      print("============INICIAR SESIÓN COMO ADMIN============\n")
      while True:  #Este while verifica que todo se ingrese correctamente.
        ID=input("Ingrese su Identificación: ") #Ingresar el id del usuario 
        if ID not in dicc_user:   #verifica si el Id no existe en el diccionario de Usuarios para reiniciar el while.
          print("Ingrese un ID válido")
        elif ID in dicc_user:  #Verifica si el Id existe en el diccionario de Usuarios, y así poder seguir
          password=input("Ingrese su Contraseña: ")  #Solicita la contraseña
          
          if (ID!=dicc_user[ID][0]) and (password!=dicc_user[ID][3]) and (dicc_user[ID][1]!="a" or dicc_user[ID][1]!="A"): #Verifica si el Id y los datos ingresados son los correspondientes al Id
            print("Datos Errados o Usuario sin Autorización")
          elif (ID==dicc_user[ID][0]) and (password==dicc_user[ID][3]) and (dicc_user[ID][1]=="a" or dicc_user[ID][1]=="A"): #Verifica si el Id y los datos ingresados son los que estan ligados al ID, tambien si el usuario es administrados
            os.system('clear')
            print("Bienvenido Admin",dicc_user[ID][2])
            break
          else:
            print("Su usuario no tiene los Permisos Suficientes\n")

      while True: #Funciones del ADMIN
        print("==================MENÚ DE ADMIN==================")
        print("1.Agregar Inventario inicial")
        print("2.Actualizar Inventario Existente")
        print("3.Borrar Item de Inventario")
        print("4.Buscar Item en Inventario")
        print("5.Visualizar Inventario Actual")
        print("6.Menú Inicial\n")
          
        menuadmin=input("Por favor Ingrese una Opción:")#Peguntar opcion del menú anterior.
        os.system('clear')

#-----------------------------------INVENTARIO INICIAL----------------------------

        
        if menuadmin=="1": #INGRESO DE INVENTARIO INICIAL
          while True:  #Este es el while que nos dara ciclo en el inventario inicial, para trabajar sobre el.
            print("================INVENTARIO INICIAL================\n")
            while True: #Este while es el que verificará que todo se ingrese de forma correcta.
              id_producto=input("Ingrese ID del Producto a Ingresar: ") #Ingresar el Id del producto a agregar al inventario 
              if id_producto in inv_inicial: #Verifica si ya existe otro producto con el mismo Id para que no se sobreescriba.
                print("Este ID ya Existe")
              elif id_producto not in inv_inicial: #SI el Id no existe en el diccionario, entonces deja seguir con su registro
                nombre_producto=input("Ingrese el Nombre del Producto a Ingresar: ") #Solicita el nombre del producto a Ingresar
                while True: #Este while controla el siguiente Try.
                  try: #Este try verifica que los datos que se ingresaran,sean del tipo de dato correcto,entero en este caso.
                    cantidad_producto=int(input("Ingrese la cantidad del Producto a Ingresar: "))#Solicita la cantidad del item.
                    precio_producto=int(input("Ingrese el Precio del Producto(c/u): ")) #Solicita el precio por unidad.
                    break
                  except:
                    print("Ingrese un tipo de dato válido") #Si ingresan un tipo de dato que no es válido salta este mensaje.  
                inv_inicial[id_producto]=[id_producto,nombre_producto,cantidad_producto,precio_producto]#Agrega todo lo anterior a un diccionario de inventario inicial.
                print("\n")
                print("Usted agregó el Producto Exitosamente\n")
                mostrar_inventario()
                break     
              else:
                print("Ingrese Datos Válidos")
            print("\n")    
            seguir_inv=input("¿Va a realizar otro Ingreso? (SI/NO):")  #Pregunta si se va a agregar otro producto mas, para seguir en el modulo.
            if seguir_inv=="si" or seguir_inv=="SI" or seguir_inv=="Si" : #Si se escoge si, reinicia el while para seguir.
              os.system('clear')
              print("Ingrese otro producto")
            elif seguir_inv=="no" or seguir_inv=="NO" or seguir_inv=="No": #si se escoge No, te devuelve al menú de admin
              os.system('clear')
              break
            else:
              print("Opción Inválida")

              
#----------------------------------ACTUALIZAR INVENTARIO---------------------------           
       
        elif menuadmin=="2": #ACTUALIZAR INVENTARIO
          print("============ACTUALIZACIÓN DE INVENTARIO============\n")
          mostrar_inventario()
          
          while True:
            print("=================================================\n")
            print("¿Qué Desea Hacer?")
            print("1.Agregar Cantidad a Item ya Existente")
            print("2.Modificar un Item Totalmente\n")
            agregar_inv=input("Seleccione una Opcción:") #Pregunta la opccion del menú anterior.
            if agregar_inv=="1": #Esta opción es para agregarle cantidades a un Item que ya existe.
              print("==========MODIFICACIÓN CANTIDAD DE ITEM===========\n")
              id_producto=input("Ingrese ID del Producto a Actualizar:") #Pregunta el Id del Item existente.
              print("","ID del Producto:",inv_inicial[id_producto][0],"\n","Nombre del Producto:",inv_inicial[id_producto][1],"\n","Cantidad en Existencia:",inv_inicial[id_producto][2],"\n","Precio por Unidad:","$",inv_inicial[id_producto][3],"\n")#Imprime el estado actual del prodcto a actualizar.
              modificacion_producto=inv_inicial[id_producto][2]+int(input("Ingrese la cantidad del Producto a Agregar:"))#Toma el producto y su cantidad actual, y le suma la cantidad a agregar.esta la guarda en una variable.
              inv_inicial.update({id_producto:[id_producto,inv_inicial[id_producto][1],modificacion_producto,inv_inicial[id_producto][3]]}) #Actualiza el inventario teniendo en cuenta la nueva cantidad que quedará utilizando la variable anterior.
              os.system('clear')
              print("Usted actualizó el Producto Exitosamente\n")
              mostrar_inventario()
              break
            elif agregar_inv=="2": #MODIFICACIÓN DEL INVENTARIO
              print("============MODIFICACIÓN DE INVENTARIO=============\n")
              id_producto=input("Ingrese ID del Producto a Actualizar:") #Ingresar el id a actualizar
              nombre_producto=input("Ingrese el Nombre del Producto a Actualizar:") #Ingresar el nombre del producto a actualizar
              cantidad_producto=int(input("Ingrese la cantidad del Producto a Actualizar:")) #Ingresar la cantidad de producto a actualizar
              precio_producto=int(input("Ingrese el Precio del Producto(c/u) a Actualizar:"))#Ingresar el precio de producto a actualizar
              inv_inicial.update({id_producto:[id_producto,nombre_producto,cantidad_producto,precio_producto]})#Actualiza el inventario con los datos ingresados
              os.system('clear')
              print("Usted actualizó el Producto Exitosamente\n") 
              print("El Inventario Actual es:")#Impresion del inventario actualizado.
              print("Referencia     Descripción    Cantidad   Valor Total")
              for i in inv_inicial:
                print(f'{inv_inicial[i][0]:17}{inv_inicial[i][1]:10}{inv_inicial[i][2]:8}{"":8}{"${:.0f}".format(inv_inicial[i][3]):10}')
              break

#----------------------------------------------------------ELIMINAR DEL INVENTARIO-----------------------------------------------

              
        elif menuadmin=="3": #ELIMINAR DEL INVENTARIO
          print("============ELIMINAR DEL INVENTARIO============\n")
          mostrar_inventario()
          
          print("===============================================\n")
          id_producto=input("Ingrese el ID a Eliminar:") #Pregunta el Id a Eliminar.
          if id_producto in inv_inicial:#Busca si el Id existe en el diccionario y lo elimina
            inv_inicial.pop(id_producto)
            print("El Id",id_producto,"Se ha eliminado con Éxito")
            mostrar_inventario()
            
          elif id_producto not in inv_inicial: #Si el Id no existe en el diccionario, salta un mensaje
            print("El Id Ingresado no existe")
          else:
            print("Ingrese un Dato Válido")


#----------------------------------------BUSCAR EN EL INVENTARIO------------------

            
        elif menuadmin=="4": #BUSCAR EN EL INVENTARIO
          print("============BUSCAR EN EL INVENTARIO============\n")
          id_producto=input("Ingrese el Id a Buscar:") #Pregunta el Id del producto a buscar
          print(" ID:",inv_inicial[id_producto][0],"\n","Nombre del Producto:",inv_inicial[id_producto][1],"\n","Cantidad en Existencia:",inv_inicial[id_producto][2],"\n","Precio por Unidad:","$",inv_inicial[id_producto][3]) #Imprime el Id del producto buscado.


#-----------------------------------------VER INVENTARIO ACTUAL--------------------

          
        elif menuadmin=="5":  #OBSERVAR EL INVENTARIO
          print("====================INVENTARIO====================")
          mostrar_inventario()
          
        elif menuadmin=="6": #SALIR DEL MENÚ
          os.system('clear')
          break

          
#-----------------------------------------INICIAR SESÍON COMO VENDEDOR-------------

          
    elif menu=="3": #INICIAR SESIÓN VENDEDOR
      print("============INICIAR SESIÓN COMO VENDEDOR============\n")
      while True:
        ID=input("Ingrese su Identificación:") #Preguntar el Id del Usuario.
        if ID not in dicc_user:  #Si el Id no esta en el Diccionario de Usuarios salta error.
          print("Ingrese un ID válido")
        elif ID in dicc_user: #Si el Id está en el Diccionario Deja seguir.
          password=input("Ingrese su Contraseña:") #Pregunta contraseña.
          if (ID!=dicc_user[ID][0]) and (password!=dicc_user[ID][3]) and (dicc_user[ID][1]!="a" or dicc_user[ID][1]!="A" or dicc_user[ID][1]!="v" or dicc_user[ID][1]!="V"): #Verifica si el Id y los datos ingresados son los correspondientes al Id
            print("Datos Errados o Usuario sin Autorización")
          elif (ID==dicc_user[ID][0]) and (password==dicc_user[ID][3]) and (dicc_user[ID][1]=="a" or dicc_user[ID][1]=="A") or (dicc_user[ID][1]=="v" or dicc_user[ID][1]=="V"): #Verifica si el Id y los datos ingresados son los que estan ligados al ID, tambien si el usuario es administrados
            os.system('clear')
            print("Bienvenido Vendedor",dicc_user[ID][2])
            break
          else:
            print("Ingrese datos válidos\n")

#-------------------------------------MENÚ DEL VENDEDOR-------------------------

            
      while True: #MENÚ DEL VENDEDOR
        print("==================MENU DE VENDEDOR==================") #Imprimir menu de vendedor
        print("1.Facturar")
        print("2.Ver Inventario Actual")
        print("3.Ver Ganancias")
        print("4.Salir\n")
        menuvende=input("Por Favor Ingrese una Opción:") #Preguntar la opccion del menú
        os.system('clear')

#-------------------------------------FACTURACIÓN--------------------------------

        
        if menuvende=="1": #FACTURACIÓN
          print("==================FACTURACIÓN===================\n")
          mostrar_inventario()  
          while True:  #While que controla los datos ingresados en la facturación.
            print("================================================\n")
            id_producto=input("Ingrese el Id a Facturar:") #Pregunta Id del producto a facturar.
            print("","ID:",inv_inicial[id_producto][0],"\n","Nombre del Producto:",inv_inicial[id_producto][1],"\n","Cantidad en Existencia:",inv_inicial[id_producto][2],"\n","Precio por Unidad:","$",inv_inicial[id_producto][3]) #Imprimir producto y sus datos a facturar.
            print("================================================\n")
            cantidad_vender=int(input("Ingrese la Cantidad a Facturar:")) #Pregunta la cantidad a facturar.
            while True: #While que controla los descuentos dados.
              descuento=int(input("Ingrese el decuento a Otorgar(0,5,10,20)%:")) #Pregunta cantidad de descuento.
              if descuento==0 or descuento==5 or descuento==10 or descuento==20:  #Condicionales que verifican los datos del descuento.
                descuento_venta=descuento/100
                descuento_valor=((inv_inicial[id_producto][3]*cantidad_vender)*descuento_venta)
                lista_descuento[id_producto]=[descuento_valor]
                valor_facturar=(inv_inicial[id_producto][3]*cantidad_vender)-descuento_valor #Calcular el valor a facturar dismunuyendo el descuento otorgado.
                lista_compras[id_producto]=[id_producto,inv_inicial[id_producto][1],cantidad_vender,valor_facturar] #Agrega lo que se va a facturar a un Diccionario que será nuestra lista de compras
                break
              elif descuento!=0 or descuento!=5 or descuento!=10 or descuento!=20:
                print("Ingrese un Descuento Válido")
              else:
                print("Ingrese un Dato Válido")
            print("Usted está Facturando:")  #Imprime la Lista de Compras actual.
            print("","ID:",inv_inicial[id_producto][0],"\n","Nombre del Producto:",inv_inicial[id_producto][1],"\n","Cantidad a facturar:",cantidad_vender,"\n")
            cantidad_productopv=inv_inicial[id_producto][2]-lista_compras[id_producto][2] #Calcula la cantidad que quedara del item a facturar, restandole al inventario la cantidad a facturar.
            inv_inicial.update({id_producto:[id_producto,inv_inicial[id_producto][1],cantidad_productopv,inv_inicial[id_producto][3]]}) #Actualizar el Inventario, restando la cantidad a facturar.
            mostrar_compras()
            
            print("================================================\n")
            facturar_mas=input("¿Desea Facturar otro Producto? (SI/NO):") #Pregunta si se va a agregar mas items a la compra
            os.system('clear')
            if facturar_mas=="SI" or facturar_mas=="si" or facturar_mas=="Si": #Si se escogé que si, imprime el inventario actual y reinicia el ciclo de facturación.
              mostrar_inventario()
              
              print("¡Ingrese el Otro Producto a Facturar!") 
            elif facturar_mas=="NO" or facturar_mas=="no" or facturar_mas=="No":
              confirmar_venta=input("¿Desea Facturar los Productos Anteriores? (SI/NO):") #Pregunta si se va a Facturar lo de la lista de compras
              os.system('clear')
              while True:
                if confirmar_venta=="SI" or confirmar_venta=="si" or confirmar_venta=="Si": #Si se escoge que si, sigue con la facturación.
                  valor_total=0
                  descuento_total=0
                  for i in lista_compras: #Se crea un acumulador, donde toma cada precio de la lista de compras y las suma dando un valor total
                    valor_total=valor_total+lista_compras[i][3]
                    descuento_total=descuento_total+lista_descuento[i][0] #Toma cada descuento de cada item y lo suma, dando un valor total.
                  mostrar_inventario()
                  
                  print("____________________________________________________\n")
                  mostrar_compras()
                  
                  print("____________________________________________________\n")
                  cliente=input("Ingrese Nombre del Cliente:") #Pregunta todos los datos del cliente para generar la factura.
                  idcliente=input("Ingrese Id del Cliente:")
                  direccioncliente=input("Ingrese Dirección del Cliente:")
                  telefonocliente=input("Ingrese Teléfono del Cliente:")
                  subtotal = (valor_total/1.12) #Calcula el subtotal, Valor de todo sin el IVA.
                  iva=((subtotal)*12)/100 #Calcula el IVA por aparte para relacionarlo en la factura..
                  os.system('clear')
                  print("==================FACTURA DE VENTA==================")  #Se imprime toda la factura.
                  print("                      AJASITOSNO                    ")
                  print("                  NIT.192.168.001.100               ")
                  print("             Santiago de Cali-Tel:3230101           ")
                  print("            Resolución DIAN 124894165319841         ")
                  print("              Autorizada el:", datetime.today().strftime('%Y-%m-%d')) #Se usa la libreria datetime para imprimir fecha.
                  print("                 Vigencia:6 Meses                   ")
                  print("                Responsable de IVA                  ")
                  print("             Actividad Economica 1730               ")
                  print("____________________________________________________\n")
                  print("Fecha:",datetime.today().strftime('%Y-%m-%d %H:%M')) #Se usa la libreria datetime para fecha y hora actual.
                  print("Cliente:",cliente)    #Imprime todos los datos del cliente.
                  print("CC/NIT:",idcliente)
                  print("Dirección:",direccioncliente)
                  print("Teléfono:",telefonocliente)
                  print("____________________________________________________\n")
                  print("                 PRODUCTOS COMPRADOS                \n")
                  print("Referencia     Descripción    Cantidad   Valor Total\n")#Imprime la lista de compras.
                  for i in lista_compras:
                    print(f'{lista_compras[i][0]:17}{lista_compras[i][1]:10}{lista_compras[i][2]:8}{"":8}{"${:.0f}".format(lista_compras[i][3]):10}')
                  print("____________________________________________________\n")
                  print("SUBTOTAL:","$","{:.0f}".format(subtotal))  #Imprime todos los datos en cuanto a valores de forma discriminada.
                  print("DESCUENTO:","$","{:.0f}".format(descuento_total))
                  print("IVA:","$","{:.0f}".format(iva))
                  print("TOTAL:","$","{:.0f}".format(subtotal+iva))
                  print("____________________________________________________\n")
                  print("                 ¡GRACIAS POR SU COMPRA!                 \n") 
                  ganancias.append(subtotal)  #Agrega la ganancia a una lista donde se guardan los descuentos por factura.
                  lista_compras.clear() #Limpia la lista de compras, para que se comience denuevo a facturar.
                  break
                elif confirmar_venta=="NO" or confirmar_venta=="no" or confirmar_venta=="No": #Si se selecciona que no se va a facturar, devuelve las cantidades sacadas al inventario, dejandolo tal cual como estaba.
                  for i in lista_compras:
                    cantidad_productopv=inv_inicial[i][2]+lista_compras[i][2]
                    inv_inicial.update({i:[i,inv_inicial[i][1],cantidad_productopv,inv_inicial[i][3]]})
                    lista_compras.clear()
                    break
                  lista_compras.clear()
                  mostrar_inventario() 
                  
                else:
                    print("Ingrese datos validos")  
                break
              break    
            
            else:
              print("Ingrese Datos Válidos")
              break
          break 

#---------------------------------------------------- VER INVENTARIO-------------------------------------------  

          
        elif menuvende=="2": #VER INVENTARIO ACTUAL
          mostrar_inventario()
          
#---------------------------------------------------VER GANANCIAS----------------------------

            
        elif menuvende=="3":
          print("===================GANANCIAS===================")
          ganancia_acumula=0
          for i in ganancias: #Suma todas las ganancias facturadas que se encuentran en la lista generada.
            ganancia_acumula=ganancia_acumula+i
          print("Las Ganancias Totales son:${0:.0f}".format((ganancia_acumula*10)/100)) #Toma el valor total y le saca el 10% que es correspondiente a las ganancias.
        elif menuvende=="4":
          print("¡Usted ha salido!")
          break
    elif menu=="4":
      print("¡Vuelva Pronto!") #Salirse del programa.
      break
    
    else:
      print("¡Escoja una Opción Válida!")
config_inicial()