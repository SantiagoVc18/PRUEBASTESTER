En esta carpeta realice dos archivos diferentes que hacen lo mismo pero uno es por paginas y el otro es por cada metodo que realiza la pagina va hacer la simulacion de ese metodo uno por uno
locustfile es uno es el que tiene todos los metodos relacionado al crud como tal 
el locustfileprueba2  es el que hace las pruebas por pagina


estos son los comando para la terminal : 
-pip install locust  y tambien instalelo aparte en la pagina oficial
-Python manage.py runserver   primero inicializarlo para que corra la pagina 
-cd authentapp/test/   y abrir otra terminal luego estar ubicado bien en que carpeta tiene los archivos en ese terminal en donde va correr el locust
-locust -f locustfile.py  Con este comando se inicia el locust te genera un localhost aparte donde te visualiza para hacer las pruebas y donde dice host en el framework poner el localhost que tiene el proyecto.
