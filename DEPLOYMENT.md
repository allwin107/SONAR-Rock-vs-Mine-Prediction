# Deployment Guide

## Deploy to Vercel

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. Go to [Vercel](https://vercel.com)
2. Sign in with your GitHub account
3. Click "Add New Project"
4. Import your GitHub repository: `allwin107/SONAR-Rock-vs-Mine-Prediction`
5. Vercel will automatically detect the configuration from `vercel.json`
6. Click "Deploy"
7. Wait for the deployment to complete
8. Your app will be live at `https://your-project-name.vercel.app`

### Option 2: Deploy via Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy from the project directory:
   ```bash
   vercel
   ```

4. Follow the prompts to complete deployment

5. For production deployment:
   ```bash
   vercel --prod
   ```

## Important Notes

- The model will be trained automatically during the first request if not present
- All dependencies are listed in `api/requirements.txt`
- The application uses Flask in serverless mode
- Static files (CSS, JS) are served from the `static` folder
- Templates are served from the `templates` folder

## Environment Variables

No environment variables are required for basic deployment.

## Troubleshooting

If you encounter issues:

1. Check the Vercel deployment logs
2. Ensure all dependencies are listed in `api/requirements.txt`
3. Verify that `sonar data.csv` is included in the repository
4. Make sure the model training completes successfully

## Local Testing

Before deploying, test locally:

```bash
python app.py
```

Then visit `http://localhost:5000` in your browser.
