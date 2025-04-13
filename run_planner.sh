#!/bin/bash

echo "📅 Running Smart Planner..."
python3 planner.py

# Optional Git logging
git add planner_*.txt
git commit -m "🗓️ Weekly planner generated: $(date +'%Y-%m-%d')"
git push origin main
