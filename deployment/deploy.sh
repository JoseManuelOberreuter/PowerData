#!/bin/bash

# Deployment script for PowerData
# Usage: ./deploy.sh [environment] [version]

set -e

ENVIRONMENT=${1:-development}
VERSION=${2:-latest}

echo "Starting PowerData deployment"
echo "Environment: $ENVIRONMENT"
echo "Version: $VERSION"

# Validate we are in the correct directory
if [ ! -f "../main.py" ]; then
    echo "Error: This script must be run from the deployment/ directory"
    exit 1
fi

# Build the image
echo "Building Docker image..."
docker build -t powerdata:$VERSION -f ../Dockerfile ..

# Stop existing containers
echo "Stopping existing containers..."
docker-compose down || true

# Start services
echo "Starting services..."
docker-compose up -d

# Verify application is running
echo "Verifying application is running..."
sleep 10

if curl -f http://localhost:8000/api/health > /dev/null 2>&1; then
    echo "Deployment successful! Application is running at http://localhost:8000"
else
    echo "Error: Application is not responding"
    docker-compose logs powerdata-app
    exit 1
fi

echo "Deployment completed successfully!"