from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
        
    def on_start(self):
        # Autenticación al iniciar las pruebas
        self.login()

    def login(self):
        # Simular el inicio de sesión con el email y password correcto
        response = self.client.post("/login/", {
            "email": "juan@gmail.com",  # Usa un email que esté registrado
            "password": "SANTIVC20"  # Asegúrate de que la contraseña sea correcta
        })

        # Comprobar si la autenticación fue exitosa
        if response.status_code == 200:
            print("Login exitoso")
        else:
            print("Error en el login")

    @task(1)
    def load_home(self):
        # Cargar la página principal
        self.client.get("/")

    @task(2)
    def signup_usu(self):
        # Simular el registro de un nuevo usuario empleado
        self.client.post("/signup_usu/", {
            "your_email": "newuser@example.com",
            "password": "password123",
            "repassword": "password123",
            "first_name": "Nuevo",
            "last_name": "Usuario",
            "doc_id": "123456789",
            "code": "+57",
            "phone": "321654987",
            "titles[]": ["Ingeniero Civil"]
        })

    @task(3)
    def signup_con(self):
        # Simular el registro de una nueva compañía
        self.client.post("/signup_con/", {
            "your_email": "newcompany@example.com",
            "password": "password123",
            "repassword": "password123",
            "first_name": "Nueva",
            "nit_id": "900123456",
            "code": "+57",
            "phone": "987654321"
        })

    @task(4)
    def crear_proyecto(self):
        # Crear un nuevo proyecto
        self.client.post("/nuevo-proyecto/", data={
            "title": "Nuevo Proyecto",
            "description": "Descripción del proyecto",
            "start-date": "2023-01-01",
            "end-date": "2023-12-31",
            "presupuesto": 10000
        })
    
    @task(5)
    def editar_proyecto(self):
        # Editar un proyecto
        self.client.post("/projects/edit/1/", data={
            "name": "Proyecto Editado",
            "description": "Descripción actualizada"
        })

    @task(6)
    def eliminar_proyecto(self):
        # Eliminar un proyecto
        self.client.post("/eliminar-proyecto/1", data={"id_proyecto": 1})


    @task(7)
    def crear_tarea(self):
        # Crear una nueva tarea
        self.client.post("/nueva-tarea/1", data={
            "title": "Nueva Tarea",
            "description": "Descripción de la tarea",
            "start-date": "2023-01-01",
            "end-date": "2023-12-31",
            "presupuesto": 5000,
            "status": 1
        })

    @task(8)
    def editar_tarea(self):
        # Editar una tarea existente
        self.client.post("/editar-tarea/1/", data={
            "title": "Tarea Editada",
            "description": "Descripción actualizada de la tarea",
            "start-date": "2023-02-01",
            "end-date": "2023-12-31",
            "presupuesto": 6000
        })    

    @task(9)
    def eliminar_tarea(self):
        # Eliminar una tarea
        self.client.post("/eliminar-tarea/1", data={"id_tarea": 1})

    @task(10)
    def actualizar_perfil(self):
        """Simular la actualización de perfil del usuario"""
        self.client.post("/actualizar_perfil/", {
            "first_name": "NuevoNombre",
            "last_name": "NuevoApellido",
            "username": "nuevo_usuario",
            "password": "nuevo_password123"
        })

    @task(11)
    def buscar_usuario(self):
        # Buscar un usuario
        self.client.get("/buscar-usuario/", params={"query": "testuser"})

    @task(12)
    def agregar_usuario(self):
        # Agregar un usuario a un proyecto
        self.client.post("/agregar-usuario/", data={
            "projectId": 1,
            "userEmail": "testuser@example.com",
            "rolUser": 1
        })
    
    @task(13)
    def proyectos_info(self):
        """Simular la consulta de proyectos"""
        self.client.get("/proyectos/")


    @task(14)
    def signout(self):
        # Cerrar sesión
        self.client.get("/logout/")
    
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)
    