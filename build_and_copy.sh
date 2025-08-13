#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install frontend dependencies & build
cd frontend
npm install
npm run build
cd ..

# Copy build into backend/static
rm -rf backend/static
mkdir -p backend/static
cp -r frontend/build/* backend/static/

# Install backend dependencies
pip install -r backend/requirements.txt
