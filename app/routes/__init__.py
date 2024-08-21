# app/routes/__init__.py

# This file allows the routes directory to be treated as a package.
# You can use it to import your routes so they are automatically available
# when the package is imported.

from .auth import router as auth_router
