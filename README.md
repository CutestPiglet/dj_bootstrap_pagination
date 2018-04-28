Dj Bootstrap Pagination
=======================

| | | |
|-|-|-|
|Author|Robert Chiang|
|Version|`0.1.0`|
|Description|`Dj Bootstrap Pagination` is based on Django's core paginator module, and the pager is rendered using Bootstrap 3.x. But only Previous Page and Next Page is provided so far.|
|Requirements|`Python 2.x` or `Python 3.x`<br>`Django 1.6+`|

Installation
============

1. Install `Dj Bootstrap Pagination` from PyPI:  
  `pip install dj-bootstrap-pagination`

1. Append `dj_bootstrap_pagination` to `INSTALLED_APPS` settings:
   ``` python
   INSTALLED_APPS = (
       ...,
       ...,
       ...,
       'dj_bootstrap_pagination',
   )
   ```

Usage
=====

* **views.py**
  ``` python
  from django.contrib.auth.models import User
  from dj_bootstrap_pagination.paginator import BootstrapPaginator

  users = User.objects.filter(is_active=True)
  items_per_page = 30

  paginator = BootstrapPaginator(users, items_per_page)
  try:
      users = paginator.page(request)
  except PageNotAnInteger:
      users = paginator.page(1)
  except EmptyPage:
      users = None

  return render(request, 'your_template.html', {'users': users})
  ```

* **your_template.html**
  ``` python
  {% for user in users %}
    ...
    ...
    ...
  {% endfor %}

  {{ users.render_pager }}
  ```

* **settings.py** (optional)
  ``` python
  DJ_BOOTSTRAP_PAGINATION_SETTINGS = {
      'PAGE_NUMBER_QUERY_STRING': 'page',  # set url query string name, default name is page
  }
  ```

TODO
====

* Support Boostrap 4.x
* Show page numbers
* Add more available `DJ_BOOTSTRAP_PAGINATION_SETTINGS`

