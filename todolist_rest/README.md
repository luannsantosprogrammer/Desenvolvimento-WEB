# 📝 Todo API

[![Python](https://img.shields.io/badge/Python-3.12+-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.20+-orange)](https://www.django-rest-framework.org/)

Uma **API REST de gerenciamento de tarefas (ToDo)** construída com **Django Rest Framework**. Permite criar, listar, atualizar e deletar tarefas de forma segura, cada usuário acessando apenas suas próprias tarefas.

---

## 🚀 Funcionalidades

* 🔒 Autenticação de usuários
* ✅ CRUD completo de tarefas:

  * Criar nova tarefa
  * Listar todas as tarefas do usuário
  * Atualizar título e status de conclusão
  * Deletar tarefas
* 🛠 Admin customizado para fácil visualização

---

## 🛠 Tecnologias

* Python 3.12+
* Django 5.x
* Django REST Framework
* SQLite (ou outro banco configurável)

---

## 🗂 Estrutura do Projeto e Explicação de Código

### `app/models.py`

Define o modelo `Task`:

```python
class Task(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

* `user`: vincula a tarefa ao usuário que a criou.
* `title`: título da tarefa.
* `completed`: indica se a tarefa foi concluída.
* `created_at`: data de criação automática.

---

### `app/admin.py`

Customiza a visualização de tarefas no Django Admin:

```python
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','completed','created_at']
    list_filter = ['title','completed','created_at']
admin.site.register(Task, TaskAdmin)
```

* `list_display`: mostra colunas importantes na lista de tarefas.
* `list_filter`: permite filtrar tarefas por título, status e data.

---

### `app/serializers.py`

Serializador para a API:

```python
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["user", "created_at"]
```

* `fields = "__all__"`: inclui todos os campos do modelo.
* `read_only_fields`: impede que usuário envie `user` ou `created_at` no POST, eles são gerados automaticamente.

---

### `app/views.py`

Views da API usando **generics** do DRF:

**Lista e cria tarefas (`GET`/`POST`)**

```python
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticated]    

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

* Retorna apenas tarefas do usuário logado.
* Salva automaticamente o usuário ao criar uma tarefa.

**Detalhes, atualização e exclusão (`GET`/`PUT`/`DELETE`)**

```python
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
```

* Garante que o usuário só acesse suas próprias tarefas.

---

### `app/urls.py`

URLs da app:

```python
urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name='task-list'),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name='task-detail'),
    path('tasks/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tasks/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

* `/tasks/`: lista e cria tarefas.
* `/tasks/<id>/`: detalhes, atualização e exclusão de tarefas.
* `path('tasks/token/', TokenObtainPairView.as_view(), name='token_obtain_pair')`: rota de autentificação de usuário.
* `path('tasks/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')`: rota onde o usuário solicita novo código de acesso

---

### `todo_api/urls.py`

URLs do projeto:

```python
urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
```

* Inclui as URLs da app e do admin.

---

## ⚡ Endpoints

| Método | Endpoint       | Descrição                         | Autenticação   |
| ------ | -------------- | --------------------------------- | -------------- |
| GET    | `/tasks/`      | Lista todas as tarefas do usuário | 🔒 Obrigatório |
| POST   | `/tasks/`      | Cria uma nova tarefa              | 🔒 Obrigatório |
| GET    | `/tasks/<id>/` | Retorna detalhes de uma tarefa    | 🔒 Obrigatório |
| PUT    | `/tasks/<id>/` | Atualiza uma tarefa               | 🔒 Obrigatório |
| DELETE | `/tasks/<id>/` | Deleta uma tarefa                 | 🔒 Obrigatório |

---

## ⚙️ Rodando o Projeto Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/todo_api.git
cd todo_api
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Rode as migrações:

```bash
python manage.py migrate
```

4. Crie um superusuário (opcional, para acessar admin):

```bash
python manage.py createsuperuser
```

5. Execute o servidor:

```bash
python manage.py runserver
```

6. Acesse a API em: `http://127.0.0.1:8000/tasks/`
   Django Admin em: `http://127.0.0.1:8000/admin/`

---

## 💡 Observações

* Todos os endpoints exigem autenticação (`IsAuthenticated`).
* Campos `user` e `created_at` são gerados automaticamente.
* Fácil de estender para adicionar **categorias**, **prioridade**, **data de vencimento** ou outros campos.



