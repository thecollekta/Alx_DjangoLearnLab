# Django Blog Project

## Overview

This Django blog project provides a full-featured blog system where users can:

- **Register**, **login**, and **manage their profiles**.
- Create, read, update, and delete (CRUD) blog posts.
- View a list of all posts and detailed views for each post.
- Permissions ensure that only authors can edit or delete their own posts.

## Features

### 1. User Authentication

- **Registration**: Users can register an account by providing their email, username, and password.
- **Login/Logout**: Users can log in and log out securely.
- **Profile Management**: Logged-in users can view and update their profile, including editing their email and other details.

### 2. Blog Post Management (CRUD)

- **Post Creation**: Authenticated users can create a new blog post with a title and content. The logged-in user is automatically set as the post author.
- **Post Listing**: All users (authenticated or not) can view a list of all blog posts. Posts are ordered by their publication date.
- **Post Detail**: All users can view detailed information about a specific post by clicking on the post title in the list view.
- **Post Update**: Only the author of a post can edit it. This functionality is restricted to the logged-in user who created the post.
- **Post Deletion**: Similarly, only the post author can delete their post. The user is asked for confirmation before the post is deleted.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/thecollekta/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab
cd django_blog
```

### 2. Install Dependencies

Create a virtual environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\\Scripts\\activate  # For Windows
pip install -r requirements.txt
```

### 3. Configure the Database

Apply migrations to set up the database:

```bash
python manage.py migrate
```

### 4. Create a Superuser

To access the Django admin and manage users and posts, create a superuser:

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Access the blog at `http://127.0.0.1:8000/`.

## Blog Post Management Features

### 1. Create a New Post

- URL: `/post/new/`
- Requires authentication.
- Form to input a title and content for the post.

### 2. List All Posts

- URL: `/`
- Displays all posts with a title and a snippet of content.
- Accessible to all users.

### 3. View Post Details

- URL: `/post/<int:pk>/`
- Shows the full content of a post, along with its author and publication date.
- Accessible to all users.

### 4. Edit a Post

- URL: `/post/<int:pk>/update/`
- Requires authentication.
- Only the author of the post can edit it.

### 5. Delete a Post

- URL: `/post/<int:pk>/delete/`
- Requires authentication.
- Only the author of the post can delete it, with confirmation.

### Permissions and Access Control

**Authenticated Users**: Can create, edit, and delete their own posts. They can also view and update their profile.

**Unauthenticated Users**: Can view the list of blog posts and individual post details but cannot create, edit, or delete posts.

### Security Considerations

- **CSRF Protection**: All forms in the project are protected by CSRF tokens to prevent cross-site request forgery.
- **Password Handling**: Django’s built-in authentication system uses hashed passwords for security.
- **Access Control**: Only authors can edit or delete their posts, ensuring that no unauthorized changes occur.

### How to Test the Features

1. **Registration**: Visit `/register/` to create a new user.
2. **Login**: Go to `/login/` and log in with your credentials.
3. **Create a Post**: Once logged in, navigate to `/post/new/` to create a blog post.
4. **View Posts**: The home page (`/`) lists all posts. Click on a post to view its details.
5. **Edit/Delete Posts**: As the post author, you’ll see links to edit or delete your posts.

### Future Improvements

- Add comments to blog posts.
- Implement tagging and categorization of posts.
- Add a rich-text editor for better formatting of blog post content.
- Include pagination in the post list view.

## Comment System

### Features

- Authenticated users can post comments on blog posts.
- Comment authors can edit or delete their own comments.
- Comments are displayed below the corresponding blog post.
- The comment form is only visible to authenticated users.

### Models

- `Comment` model includes:
  - `post`: ForeignKey linking to the `Post`.
  - `author`: ForeignKey linking to `User`.
  - `content`: TextField for comment content.
  - `created_at`: DateTime when the comment was created.
  - `updated_at`: DateTime when the comment was last modified.

### Forms

- `CommentForm`: Form used for creating and editing comments.

### Views

- `add_comment`: Handles creating new comments.
- `edit_comment`: Allows comment authors to edit their comments.
- `delete_comment`: Allows comment authors to delete their comments.

### URL Patterns

- `/post/<int:pk>/`: Displays post details and associated comments.
- `/post/<int:post_id>/comments/new/`: Allows users to add a new comment.
- `/comment/<int:comment_id>/edit/`: Allows comment editing.
- `/comment/<int:comment_id>/delete/`: Handles comment deletion.

### Templates

- `post_detail.html`: Displays the post details and a comment section.
- `add_comment.html`: Form for adding a comment.
- `edit_comment.html`: Form for editing a comment.
