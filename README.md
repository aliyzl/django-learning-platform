# Django Learning Platform

A comprehensive bilingual (Persian/English) Django learning platform with AI-powered assistance using Gemini Flash 2.5.

## Features

- 🌍 **Bilingual Support**: Full Persian and English language support with RTL layout
- 🤖 **AI Assistant**: Integrated Gemini Flash 2.5 API for contextual Q&A
- 💻 **Platform-Specific Instructions**: Separate code examples for Windows and Mac
- 📚 **Comprehensive Course Content**: Django from zero to master level
- 🎨 **Beautiful UI/UX**: Modern, responsive design with dark/light theme
- 📝 **Interactive Code Editor**: CodeMirror integration for exercises
- 📊 **Progress Tracking**: Track your learning progress

## Installation

### Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup

1. **Clone or navigate to the project directory**

2. **Create and activate virtual environment**

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Mac/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file or set environment variables:
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key-here"
   export GEMINI_API_KEY_2="your-second-gemini-api-key-here"  # Optional, for fallback
   export SECRET_KEY="your-secret-key-here"
   export DEBUG=True
   ```
   
   **Note**: The platform supports multiple API keys for high availability. If the primary key fails or hits rate limits, it will automatically fallback to the second key. For deployment, it's recommended to set both keys.

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create course content**
   ```bash
   python manage.py create_course_content
   ```

7. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the platform**
   - Open browser: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Getting Gemini API Keys

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create API keys (you can create multiple keys)
4. Set the keys as environment variables:
   - `GEMINI_API_KEY` (required) - Primary API key
   - `GEMINI_API_KEY_2` (optional) - Secondary API key for fallback

**For Deployment**: Set both keys for high availability:
```bash
export GEMINI_API_KEY="your-gemini-api-key-here"
export GEMINI_API_KEY_2="your-second-gemini-api-key-here"
```

The system will automatically use the second key if the first one fails or encounters rate limits.

## Project Structure

```
django_learning_platform/
├── config/              # Django project settings
├── courses/             # Course management app
│   ├── models.py        # Course, Section, Lesson models
│   ├── views.py         # Course views
│   ├── admin.py         # Admin interface
│   └── management/      # Management commands
├── ai_assistant/         # AI integration app
│   ├── services.py      # Gemini API service
│   ├── views.py         # Chat endpoints
│   └── utils.py         # Context extraction
├── core/                # Core utilities
│   └── middleware.py   # Language middleware
├── templates/           # HTML templates
├── static/             # CSS, JS, images
└── locale/             # Translation files
```

## Usage

### Adding Course Content

1. **Via Admin Panel** (Recommended):
   - Access `/admin/`
   - Add courses, sections, and lessons
   - Content supports both English and Persian

2. **Via Management Command**:
   ```bash
   python manage.py create_course_content
   ```

### Language Switching

Users can switch between English and Persian using the language switcher in the navigation bar. The language preference is saved in the session.

### AI Assistant

The AI assistant is available via the chat widget (bottom right). It provides:
- Context-aware responses based on current lesson
- General Django questions
- Code explanations

### Code Editor

- Code examples are displayed with syntax highlighting
- Platform-specific examples (Windows/Mac) can be toggled
- Exercise editor allows writing and checking solutions

## Customization

### Adding More Course Content

Edit `courses/management/commands/create_course_content.py` to add more sections and lessons, or use the Django admin interface.

### Styling

Modify `static/css/style.css` to customize the appearance.

### Translations

1. Update translation files:
   ```bash
   python manage.py makemessages -l fa
   python manage.py makemessages -l en
   ```

2. Edit `.po` files in `locale/fa/LC_MESSAGES/` and `locale/en/LC_MESSAGES/`

3. Compile translations:
   ```bash
   python manage.py compilemessages
   ```

## Deployment

For production deployment:

1. Set `DEBUG=False` in settings or environment variable
2. Configure `ALLOWED_HOSTS` in settings
3. Set up proper database (PostgreSQL recommended)
4. **Configure API Keys** (Important):
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key-here"
   export GEMINI_API_KEY_2="your-second-gemini-api-key-here"
   export SECRET_KEY="your-production-secret-key"
   export DEBUG=False
   ```
   The platform supports automatic fallback between multiple API keys for high availability.
5. Collect static files: `python manage.py collectstatic`
6. Use a production WSGI server (Gunicorn, uWSGI)
7. Set up reverse proxy (Nginx)

### API Key Management

- **Multiple Keys**: The system supports multiple Gemini API keys with automatic fallback
- **High Availability**: If one key fails, the system automatically tries the next key
- **Rate Limiting**: Multiple keys help distribute load and avoid rate limits
- **Security**: Never commit API keys to version control. Always use environment variables or secure secret management services

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please check the documentation or create an issue in the repository.

