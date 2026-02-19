# Deploying Django Hotel Booking on Vercel

## Prerequisites
- GitHub repository connected
- Vercel account

## Step-by-Step Deployment

### 1. Push Your Code
```bash
git add .
git commit -m "Prepare for Vercel deployment"
git push origin master
```

### 2. Go to Vercel Dashboard
Visit: https://vercel.com/dashboard

### 3. Import Project
- Click "Add New" → "Project"
- Select your `dualityhotel` GitHub repository
- Click "Import"

### 4. Configure Environment Variables
Click "Environment Variables" and add these:

| Key | Value |
|-----|-------|
| `DJANGO_SECRET_KEY` | Generate a random key: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-project-name.vercel.app` (replace with your actual domain) |
| `PYTHON_VERSION` | `3.12` |

### 5. Build Settings
- Framework Preset: Other
- Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- Output Directory: (leave empty)
- Install Command: (leave default)

### 6. Deploy
Click "Deploy" button and wait for build to complete.

## What Happens After Deployment

Your Django app will be live at: `https://your-project-name.vercel.app`

The API handler in `/api/index.py` routes all requests to your Django WSGI application.

## Common Issues & Fixes

### Build Fails with "pip install" Error
- Check that all requirements in `requirements.txt` are compatible
- Ensure `whitenoise` is in requirements for static file serving

### Static Files Not Loading
- Static files are collected during build and served by WhiteNoise
- Verify `STATIC_ROOT` and `STATICFILES_STORAGE` settings

### Database Issues
- SQLite database (`db.sqlite3`) is created on first run
- For production, consider using a managed database service instead

## Running Migrations

First deployment will use the existing `db.sqlite3` from your repo.
To reset database on production, delete `db.sqlite3` from your repo and redeploy.

## Support
For Vercel deployment issues: https://vercel.com/help
For Django issues: https://docs.djangoproject.com
