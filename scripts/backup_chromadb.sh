#!/bin/bash

BACKUP_FILE="chroma_backup_$(date +%Y%m%d_%H%M%S).tar.gz"

echo "Backing up ChromaDB data..."
echo "======================================"

# Get the volume name
VOLUME_NAME=$(docker volume ls | grep chroma_data | awk '{print $2}')

if [ -z "$VOLUME_NAME" ]; then
    echo "✗ ChromaDB volume not found"
    exit 1
fi

echo "Volume: $VOLUME_NAME"

# Create backup
docker run --rm \
    -v $VOLUME_NAME:/data \
    -v $(pwd):/backup \
    alpine tar czf /backup/$BACKUP_FILE -C /data .

if [ $? -eq 0 ]; then
    echo "✓ Backup created: $BACKUP_FILE"
    echo ""
    echo "To restore:"
    echo "  ./scripts/restore_chromadb.sh $BACKUP_FILE"
else
    echo "✗ Backup failed"
    exit 1
fi
