## 2026-10-06 – Anonymous access baseline

- GET /recipes (anonymous) → 200 OK, returns all recipes including private ones (e.g. "Secret family hot sauce" with `is_public: false`).
- POST /recipes (anonymous) → 200/201 OK, creates a new recipe (`"API Open Test Recipe"`) even when `is_public: false`.
- DELETE /recipes/4 (anonymous) → [actual status], recipe id 4 no longer appears in GET /recipes.