#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./scripts/restore_chromadb.sh <backup_file.tar.gz>"
    exit 1
fi

BACKUP_FILE=$1

if [ ! -f "$BACKUP_FILE" ]; then
    echo "✗ Backup file not found: $BACKUP_FILE"
    exit 1
fi

echo "Restoring ChromaDB data from $BACKUP_FILE..."
echo "======================================"

# Stop ChromaDB
docker-compose down

# Get the volume name
VOLUME_NAME=$(docker volume ls | grep chroma_data | awk '{print $2}')

if [ -z "$VOLUME_NAME" ]; then
    echo "Creating volume..."
    docker volume create ${PWD##*/}_chroma_data
    VOLUME_NAME=${PWD##*/}_chroma_data
fi

echo "Volume: $VOLUME_NAME"

# Restore backup
docker run --rm \
    -v $VOLUME_NAME:/data \
    -v $(pwd):/backup \
    alpine tar xzf /backup/$BACKUP_FILE -C /data

if [ $? -eq 0 ]; then
    echo "✓ Data restored"
    
    # Start ChromaDB
    docker-compose up -d
    
    echo "✓ ChromaDB started"
    echo ""
    echo "Verify restoration:"
    echo "  python scripts/verify_persistence.py"
else
    echo "✗ Restore failed"
    exit 1
fi
