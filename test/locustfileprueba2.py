from locust import HttpUser, task, between


class UserBehavior(HttpUser):
    wait_time = between(1, 3)
    host = "http://127.0.0.1:8000/"   


    @task
    def inicio(self):
        self.client.get("/home.html")

    @task
    def login(self):
        self.client.get("/login.html")

    @task
    def Registro_usuario(self):
        self.client.get("/signup.html")    

    @task
    def Registro_con(self):
        self.client.get("/signup-con.html")

    @task
    def proyectos(self):
        self.client.get("/proyectos.html")  

    @task
    def nuevo_proyecto(self):
        self.client.get("/nuevo-proyecto.html")

    @task
    def nueva_tarea(self):
        self.client.get("/nueva-tarea.html")                  

    @task
    def base(self):
        self.client.get("/base.html")    