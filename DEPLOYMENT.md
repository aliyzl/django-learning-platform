# Deployment Guide

## Environment Variables Configuration

For production deployment, configure the following environment variables:

### Required Variables

```bash
# Django Settings
SECRET_KEY="your-production-secret-key-here"
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Gemini API Keys (Multiple keys for high availability)
GEMINI_API_KEY="your-gemini-api-key-here"
GEMINI_API_KEY_2="your-second-gemini-api-key-here"
```

### API Key Configuration

The platform supports **multiple Gemini API keys** with automatic fallback:

1. **Primary Key** (`GEMINI_API_KEY`): Required - Used as the primary API key
2. **Secondary Key** (`GEMINI_API_KEY_2`): Optional but recommended - Used as fallback

**Benefits of Multiple Keys:**
- **High Availability**: If one key fails, the system automatically uses the next key
- **Rate Limit Handling**: Distributes load across multiple keys
- **Zero Downtime**: Key rotation without service interruption

### How Fallback Works

1. System tries `GEMINI_API_KEY` first
2. If it fails or hits rate limits, automatically tries `GEMINI_API_KEY_2`
3. Logs are generated for monitoring which key is being used
4. If all keys fail, appropriate error message is returned

## Platform-Specific Deployment

### Heroku

```bash
heroku config:set GEMINI_API_KEY="your-gemini-api-key-here"
heroku config:set GEMINI_API_KEY_2="your-second-gemini-api-key-here"
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False
```

### Docker

Create a `.env` file:
```env
GEMINI_API_KEY=your-gemini-api-key-here
GEMINI_API_KEY_2=your-second-gemini-api-key-here
SECRET_KEY=your-secret-key
DEBUG=False
```

### Linux Server (systemd)

Create `/etc/systemd/system/django-platform.service`:
```ini
[Unit]
Description=Django Learning Platform
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/django
Environment="GEMINI_API_KEY=your-gemini-api-key-here"
Environment="GEMINI_API_KEY_2=your-second-gemini-api-key-here"
Environment="SECRET_KEY=your-secret-key"
Environment="DEBUG=False"
ExecStart=/path/to/venv/bin/gunicorn config.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```

### AWS/Cloud Platforms

Set environment variables in your platform's configuration:
- AWS Elastic Beanstalk: Use Environment Properties
- Google Cloud Run: Use Environment Variables in Cloud Run service
- Azure App Service: Use Application Settings
- DigitalOcean App Platform: Use Environment Variables section

## Security Best Practices

1. **Never commit API keys** to version control
2. **Use environment variables** or secure secret management services
3. **Rotate keys regularly** for security
4. **Monitor API usage** to detect anomalies
5. **Use different keys** for development and production

## Verification

After deployment, verify API keys are working:

1. Access the platform
2. Open the AI chat widget
3. Ask a question
4. Check server logs to see which API key is being used
5. Test fallback by temporarily disabling primary key

## Troubleshooting

### API Key Not Working

1. Verify keys are set correctly: `echo $GEMINI_API_KEY`
2. Check logs for API key errors
3. Verify keys are valid in Google AI Studio
4. Check rate limits and quotas

### Fallback Not Working

1. Ensure both keys are set
2. Check logs for fallback attempts
3. Verify both keys are valid
4. Check network connectivity

## Monitoring

Monitor API key usage:
- Check application logs for key rotation messages
- Monitor API quota usage in Google Cloud Console
- Set up alerts for API failures




