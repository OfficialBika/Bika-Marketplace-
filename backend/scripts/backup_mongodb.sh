#!/bin/bash

DATE=$(date +%Y-%m-%d_%H-%M)
BACKUP_DIR="backup/$DATE"

mkdir -p $BACKUP_DIR

mongodump --db bika_bot --out $BACKUP_DIR

echo "Backup completed: $BACKUP_DIR"
