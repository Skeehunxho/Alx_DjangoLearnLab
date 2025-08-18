## Django Admin Setup

To enable and access the Django admin for managing books:

1. Register the `Book` model in `bookshelf/admin.py`.
2. Create a superuser:
   ```bash
   python manage.py createsuperuser
# Permissions & Groups Setup

## Custom Permissions
Defined in `Book` model:
- can_view — View book entries
- can_create — Create book entries
- can_edit — Edit book entries
- can_delete — Delete book entries

## Groups
- Editors: can_view, can_create, can_edit
- Viewers: can_view
- Admins: all permissions

## How to Assign
1. Go to Django admin → Groups.
2. Select group → Add/remove permissions.
3. Assign users to groups via User edit page.
