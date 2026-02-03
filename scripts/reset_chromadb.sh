#!/bin/bash

echo "Resetting ChromaDB..."
echo "======================================"

# Stop and remove containers with volumes
docker-compose down -v

echo "✓ Removed containers and volumes"

# Start fresh
docker-compose up -d

echo "✓ Started ChromaDB"
echo ""
echo "Waiting for ChromaDB to be ready..."
sleep 5

# Check health
if curl -f http://localhost:8000/api/v1/heartbeat > /dev/null 2>&1; then
    echo "✓ ChromaDB is healthy"
    echo ""
    echo "Now run data ingestion:"
    echo "  python src/data_ingestion.py"
else
    echo "✗ ChromaDB is not responding"
    echo "Check logs: docker logs devops-chromadb"
fi
