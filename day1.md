# Build a Simple Django App: Geetshala (Day 1)

## 1. Install Django and Create the Project
```bash
python -m pip install Django
django-admin startproject geetshala
```

## 2. Create the `songs` App
Make sure you are in the project directory, then run:
```bash
cd geetshala
python manage.py startapp songs
```

## 3. Register the App
Open `geetshala/settings.py` and add `songs` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "songs",
]
```
*This tells Django that the `songs` app is part of the project.*

## 4. Create the `songs` Views
Open `songs/views.py` and replace its contents with:

```python
from django.http import HttpResponse
from django.shortcuts import render


def song_list(request):
    songs = [
        "Tum Hi Ho",
        "Kal Ho Naa Ho",
        "Pehla Nasha",
        "Tujh Mein Rab Dikhta Hai",
    ]

    return render(request, "songs/song_list.html", {"songs": songs})


def song_detail(request, song_name):
    return HttpResponse(f"You selected: {song_name}")
```
*Here the song list is stored directly in Python without using a database.*

## 5. Create the App URLs
Create a new file `songs/urls.py` and add:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.song_list, name="song_list"),
    path("<str:song_name>/", views.song_detail, name="song_detail"),
]
```
*The first route handles `/songs/` and the second handles `/songs/<anything>/`.*

## 6. Connect the App URLs to the Project
Open `geetshala/urls.py` and replace its contents with:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("songs/", include("songs.urls")),
]
```
*This makes all `/songs/` URLs available through the `songs` app.*

## 7. Create the HTML Template
Create these directories inside the `songs` app:

```text
songs/
└── templates/
    └── songs/
        └── song_list.html
```
*(The full path is: `songs/templates/songs/song_list.html`)*

### Create the song listing page
Add this to `song_list.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Songs</title>
</head>
<body>

    <h1>My Songs</h1>

    <ul>
        {% for song in songs %}
            <li>{{ song }}</li>
        {% endfor %}
    </ul>

</body>
</html>
```
*Django will loop through the manually defined songs list and render each song.*

## 8. Run the Server
Run the following command:

```bash
python manage.py runserver
```
*You should see something like:*
`Starting development server at http://127.0.0.1:8000/`

## 9. Test the Application

### Test `/songs/`
Open [http://127.0.0.1:8000/songs/](http://127.0.0.1:8000/songs/) in your browser. You should get:

> **My Songs**
> 
> * Tum Hi Ho
> * Kal Ho Naa Ho
> * Pehla Nasha
> * Tujh Mein Rab Dikhta Hai

### Test Dynamic Parameters
Open [http://127.0.0.1:8000/songs/tum-hi-ho/](http://127.0.0.1:8000/songs/tum-hi-ho/)
You should see:
> `You selected: tum-hi-ho`

Try another: [http://127.0.0.1:8000/songs/hello/](http://127.0.0.1:8000/songs/hello/)
You should see:
> `You selected: hello`

You can even use: [http://127.0.0.1:8000/songs/anything-you-want/](http://127.0.0.1:8000/songs/anything-you-want/)
*And Django will pass `anything-you-want` to `song_detail()`.*