# 📦 Inventory Management System

A full-featured web-based Inventory Management System built with **Django 6**,
demonstrating a complete **CRUD workflow** using **Class-Based Views (CBVs)**.

---

## 🚀 Live Features

- ✅ **Create** — Add new inventory items with price, quantity and category
- ✅ **Read** — View all items in a searchable, paginated list
- ✅ **Update** — Edit item details with a pre-filled form
- ✅ **Delete** — Remove items with a safe confirmation page
- ✅ **Low Stock Alerts** — Automatic warnings when quantity drops below 10
- ✅ **Authentication** — Login required to access all pages
- ✅ **Django Admin** — Full admin panel for superusers

---

## 🛠️ Tech Stack

| Layer        | Technology              |
|-------------|--------------------------|
| Framework    | Django 6.0.3            |
| Language     | Python 3.14             |
| Database     | SQLite3 (built-in)      |
| Frontend     | Bootstrap 5             |
| Templates    | Django Template Language |
| Auth         | Django Built-in Auth    |

---

## 📁 Project Structure
```
inventory_project/
│
├── manage.py
├── db.sqlite3
├── static/                          ← static files
│
├── templates/                       ← project-level templates
│   ├── base.html                    ← shared layout + Bootstrap navbar
│   └── registration/
│       └── login.html               ← login page
│
├── inventory_project/               ← project config
│   ├── settings.py                  ← all configuration
│   ├── urls.py                      ← root URL dispatcher
│   ├── wsgi.py
│   └── asgi.py
│
└── inventory/                       ← main application
    ├── models.py                    ← Category + InventoryItem models
    ├── views.py                     ← 5 Class-Based Views
    ├── forms.py                     ← ModelForm with validation
    ├── urls.py                      ← app-level URL patterns
    ├── admin.py                     ← Django Admin setup
    ├── apps.py
    ├── migrations/
    │   └── 0001_initial.py
    └── templates/
        └── inventory/
            ├── item_list.html       ← ListView template
            ├── item_detail.html     ← DetailView template
            ├── item_form.html       ← shared Create & Update form
            └── item_confirm_delete.html  ← Delete confirmation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/leopoldbonfils/Week-four-Assignment.git
cd inventory-management
```

### 2. Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django
```

### 4. Create the static folder
```bash
mkdir static
```

### 5. Run migrations
```bash
python manage.py makemigrations inventory
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```

### 7. Start the development server
```bash
python manage.py runserver
```

### 8. Open in browser
```
http://127.0.0.1:8000/inventory/
```

---

## 🔗 URL Reference

| URL                          | View              | Description              |
|-----------------------------|-------------------|--------------------------|
| `/accounts/login/`          | LoginView         | Login page               |
| `/inventory/`               | ItemListView      | List all items           |
| `/inventory/<pk>/`          | ItemDetailView    | View single item         |
| `/inventory/new/`           | ItemCreateView    | Add new item             |
| `/inventory/<pk>/edit/`     | ItemUpdateView    | Edit existing item       |
| `/inventory/<pk>/delete/`   | ItemDeleteView    | Delete with confirmation |
| `/admin/`                   | Django Admin      | Admin panel              |

---

## 📊 Data Models

### Category
```python
name          # CharField
description   # TextField
created_at    # DateTimeField (auto)
```

### InventoryItem
```python
name          # CharField
sku           # CharField (unique)
category      # ForeignKey → Category
quantity      # PositiveIntegerField
unit_price    # DecimalField
description   # TextField
is_active     # BooleanField
created_at    # DateTimeField (auto_now_add)
updated_at    # DateTimeField (auto_now)

# Computed Properties (not stored in DB)
total_value   # quantity × unit_price
is_low_stock  # True when quantity < 10
stock_status  # "In Stock / Low Stock / Out of Stock"
```

---

## 🧠 Class-Based Views Used

| CBV            | Purpose                              |
|---------------|--------------------------------------|
| `ListView`     | Display paginated list of all items  |
| `DetailView`   | Display single item details          |
| `CreateView`   | Handle new item form (GET + POST)    |
| `UpdateView`   | Handle edit form pre-filled (GET + POST) |
| `DeleteView`   | Confirm and delete item              |

> All views are protected with `LoginRequiredMixin`

---

## 🔐 Authentication Flow
```
User visits /inventory/
        ↓
LoginRequiredMixin checks login status
        ↓ NOT logged in          ↓ Logged in
Redirect to /accounts/login/   Show inventory list
        ↓
User submits credentials
        ↓
Redirect to /inventory/
```

---

## 💡 Key Concepts Demonstrated

- **Class-Based Views** reduce boilerplate vs Function-Based Views
- **DRY Principle** — `CreateView` and `UpdateView` share one form & template
- **ModelForm** with custom validation (`clean_sku`, `clean_unit_price`)
- **LoginRequiredMixin** protects all views from unauthenticated access
- **CSRF Protection** on all POST forms via `{% csrf_token %}`
- **Namespaced URLs** using `app_name = 'inventory'`
- **Flash Messages** for create, update and delete feedback
- **Pagination** built into `ListView` with `paginate_by = 5`

---

## 📸 Screenshots
<img width="1919" height="715" alt="Screenshot 2026-03-11 165559" src="https://github.com/user-attachments/assets/36b474a5-f87e-4af5-ad46-8598e8177be5" />

<img width="1919" height="828" alt="Screenshot 2026-03-11 165526" src="https://github.com/user-attachments/assets/b89cd565-e2c7-4d02-912a-483198b3420c" />
<img width="959" height="377" alt="image" src="https://github.com/user-attachments/assets/253af388-3ece-45d0-a48c-c5552161ef24" />
<img width="959" height="431" alt="image" src="https://github.com/user-attachments/assets/c4bbd9ad-55f0-4734-ac82-ef0af7383954" />
<img width="959" height="391" alt="image" src="https://github.com/user-attachments/assets/d100430c-7b5a-48db-9244-18ade2fc8df9" />
<img width="959" height="407" alt="image" src="https://github.com/user-attachments/assets/28721ba4-8582-421b-9726-fdc11688b13e" />
<img width="959" height="409" alt="image" src="https://github.com/user-attachments/assets/ae0bda69-17e9-4afe-81f6-f87680129a41" />


---

## 👨‍💻 Author

**Leopold MUGISHA**
- GitHub: https://github.com/leopoldbonfils
- Email: leopordbonfils@gmail.com

---

## 📄 License

This project is for educational purposes as part of a Django CRUD Assessment.

---

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Class-Based Views](https://docs.djangoproject.com/en/6.0/topics/class-based-views/)
