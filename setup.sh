#!/bin/bash
echo "Initializing GitHub Repository..."
git init
git add .
git commit -m "Automated commit for latest changes"
git remote add origin https://github.com/your-username/LLM_Booking_Analytics.git
git push -u origin main
