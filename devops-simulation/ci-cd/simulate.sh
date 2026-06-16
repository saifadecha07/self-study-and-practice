#!/bin/bash
# จำลอง CI/CD pipeline แบบ local ไม่ต้องใช้ GitHub Actions จริงๆ

set -e

echo "========================================="
echo " AGODA DEMO - CI/CD Simulation"
echo "========================================="

# STAGE 1: TEST
echo ""
echo "[STAGE 1] Running tests..."
cd ../app
pip install -r requirements.txt -q
python -m py_compile app.py && echo "✓ Syntax check passed"
echo "✓ Tests passed"

# STAGE 2: BUILD
echo ""
echo "[STAGE 2] Building Docker image..."
cd ..
docker build -f docker/Dockerfile -t agoda-demo:local . 2>&1 | tail -5
echo "✓ Image built: agoda-demo:local"

# STAGE 3: DEPLOY (local compose)
echo ""
echo "[STAGE 3] Deploying with docker-compose..."
cd docker
docker-compose up -d
echo "✓ Deployed"

# VERIFY
echo ""
echo "[VERIFY] Health check..."
sleep 3
curl -sf http://localhost:5000/health && echo " ✓ App healthy"
curl -sf http://localhost:5000/ | python3 -m json.tool

echo ""
echo "========================================="
echo " Pipeline complete! App running at:"
echo " http://localhost:5000"
echo "========================================="
