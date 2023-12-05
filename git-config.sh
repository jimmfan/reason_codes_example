#!/bin/bash

# Set your Git username and email
git config --global user.email "jimmfan@users.noreply.github.com"
git config --global user.name "jimmfan"

# Dynamically determine the project name based on the current directory
PROJECT_NAME=$(basename "$(pwd)")

# Add the safe directory configuration
git config --global --add safe.directory "/workspaces/$PROJECT_NAME"
