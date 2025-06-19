
# Django Image Upload App

This is a simple Django web application that allows users to upload images and view them in a gallery. Uploaded images are stored in the filesystem and displayed on the homepage.

## Features

- Upload images via a web form.
- View all uploaded images in a responsive gallery.
- Images are timestamped and displayed with their upload date and filename.
- Admin interface with image preview.

## Project Structure

```
image_upload/
  image/
    manage.py
    db.sqlite3
    image/
      settings.py
      urls.py
      wsgi.py
      asgi.py
    upload/
      models.py
      views.py
      forms.py
      admin.py
      urls.py
      migrations/
    templates/
      home.html
    media/
      (uploaded images)
  media/
    images/
      (uploaded images)
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd image_upload/image
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django==5.0.1 unfold
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Access the app

- Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- To access the admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Usage

- Use the form on the homepage to upload images.
- Uploaded images will appear in the gallery below the form.
- Images are stored in the `media/images/` directory.

## Notes

- This app uses SQLite by default.
- Media files are served from the `/media/` URL in development.
- For production, configure proper static and media file serving.

## Dependencies

- Django 5.0.1
- [unfold](https://github.com/unfoldadmin/unfold) (for enhanced admin interface)
- Bootstrap 5 (via CDN, for frontend styling)
- Font Awesome (via CDN, for icons)

## License

MIT License (or specify your license)

---

