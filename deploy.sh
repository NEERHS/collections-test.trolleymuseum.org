#!/bin/bash


aws --profile=devon \
  s3 sync ./ s3://trolley-collection.hubner.dev/  \
  --exclude '.git/**' \
  --exclude '.gitignore' \
  --exclude 'README.md' \
  --exclude 'LICENSE' \
  --exclude 'make_indexes.py' \
  --exclude 'cars_without_images.py' \
  --exclude '.DS_Store'


