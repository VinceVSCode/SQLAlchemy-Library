#!/bin/sh

# Step 0:Try to mount the data
echo " Mounting the data "

# Step 1: check if database exists.
echo " Check whether database exists.."

if [ ! -f /app/data/library.db ]; then
    # If not seed it.
    echo " No database found. Seeding..."
    
    python database/seed.py
else
    # We are ready to go.
    echo "✅ Database already exists. Skipping seeding."
fi

# Launch main.
echo "🚀 Launching app..."
python main.py