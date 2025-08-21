# Deploy to Render (Free)

## Quick Setup Steps:

1. **Upload your code to GitHub:**
   - Create a new repository on GitHub
   - Upload all files from this project

2. **Create Render account:**
   - Go to render.com
   - Sign up for free using your GitHub account

3. **Deploy the app:**
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Use these settings:
     - **Build Command:** `pip install -r render_requirements.txt`
     - **Start Command:** `gunicorn --bind 0.0.0.0:$PORT main:app`
     - **Python Version:** 3.11.6

4. **Environment Variables:**
   - Add SESSION_SECRET with any random string value

5. **Deploy:**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Your app will be live at the provided URL!

## Files needed for deployment:
- `render_requirements.txt` - Python dependencies
- `main.py` - Entry point for the app
- `runtime.txt` - Python version
- `render.yaml` - Optional configuration file

## Free Tier Limits:
- App sleeps after 15 minutes of inactivity
- 750 hours per month (enough for personal use)
- May take 30 seconds to wake up from sleep

Your Name Variations Finder will be completely free to run!