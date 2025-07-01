#!/bin/sh

echo " Check whether database exists.."

if [ ! -f /app/data/library.db ]; then
    echo " No database found. Seeding..."
    python database/seed.py
else
    echo "✅ Database already exists. Skipping seeding."
fi

echo "🚀 Launching app..."
python main.py