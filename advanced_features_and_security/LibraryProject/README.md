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

# Security Best Practices Implemented

## Settings
- DEBUG = False in production
- SECURE_BROWSER_XSS_FILTER, SECURE_CONTENT_TYPE_NOSNIFF, X_FRAME_OPTIONS set
- CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE enabled

## Templates
- All forms include `{% csrf_token %}` to prevent CSRF attacks.

## Views
- Django ORM used for database access (no raw SQL).
- User input validated with Django Forms.
- Example: search queries sanitized with ORM filters.

## Content Security Policy
- Configured CSP header to restrict scripts/styles to same-origin.
- Mitigates XSS injection from external sources.

## Testing
- Verified forms reject submissions without CSRF token.
- Verified users cannot inject raw SQL via query parameters.
- Checked that CSP blocks inline/external scripts.
