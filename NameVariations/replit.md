# Overview

Name Variations Finder is a Flask-based web application that helps users discover nicknames, variations, and short forms of names. The application provides both a web interface and an API endpoint for searching through a comprehensive dataset of names and their variations. Users can input a name (like "William" or "Catherine") and receive all known variations, nicknames, and alternative forms of that name.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask for server-side rendering
- **UI Framework**: Bootstrap 5 with dark theme for responsive design
- **JavaScript**: Vanilla JavaScript for form validation, search enhancements, and UI interactions
- **Styling**: Custom CSS complementing Bootstrap for enhanced visual appeal
- **Layout Structure**: Base template system with modular components for maintainability

## Backend Architecture
- **Web Framework**: Flask with Python for lightweight web application development
- **Route Structure**: Separation of web interface routes (`/`, `/search`) and API endpoints (`/api/variations`)
- **Error Handling**: Comprehensive error handling with user-friendly flash messages
- **Logging**: Built-in Python logging for debugging and monitoring
- **Session Management**: Flask sessions with configurable secret key

## Data Storage Solutions
- **In-Memory Data Store**: Python dictionaries and lists for name variations dataset
- **Data Organization**: Hierarchical structure linking base names to their variations
- **Search Logic**: Custom search functions for finding variations and base names
- **No External Database**: Self-contained dataset for simplicity and performance

## Authentication and Authorization
- **No Authentication Required**: Public application with no user accounts or permissions
- **Session Security**: Basic session secret key configuration for flash messages

## API Design
- **RESTful Endpoints**: Clean API structure for programmatic access
- **JSON Responses**: Structured JSON output for API consumers
- **Query Parameters**: Simple parameter-based search interface
- **Error Responses**: Consistent error handling for both web and API interfaces

# External Dependencies

## Frontend Libraries
- **Bootstrap 5**: UI framework from CDN for responsive design and components
- **Font Awesome 6**: Icon library from CDN for visual enhancements
- **Replit Bootstrap Theme**: Custom dark theme specifically for Replit environment

## Backend Dependencies
- **Flask**: Core web framework for Python
- **Python Standard Library**: Logging, OS modules for configuration and error handling

## Hosting Environment
- **Replit Platform**: Designed for deployment on Replit with environment variable support
- **Environment Variables**: `SESSION_SECRET` for session management configuration

## No Database Dependencies
- **Self-Contained**: No external database connections required
- **Portable**: Can run in any Python environment without additional setup

## Deployment Configuration
- **Platform**: Configured for Render.com free tier deployment
- **Dependencies**: Flask 3.1.2, gunicorn 23.0.0, email-validator 2.2.0
- **Runtime**: Python 3.11.6
- **Entry Point**: main.py with PORT environment variable support
- **Deployment Files**: render_requirements.txt, runtime.txt, render.yaml, DEPLOYMENT_INSTRUCTIONS.md