#!/usr/bin/env python3
"""Module of Index views
"""
from flask import abort, jsonify, request
from datetime import datetime

from api.v1.views import app_views


@app_views.route('/api', methods=['GET'], strict_slashes=False)
def details() -> str:
    """ GET /api
    Parameter:
      - Slack Name
      - Track
    Return:
      - User object JSON represented
    """
    slack_name = request.args.get('slack_name', '')
    track = request.args.get('track', '')
    current_day = datetime.utcnow().strftime('%A')
    utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    github_file_url = "https://github.com/110nard0/hngx_stage_1/blob/main/api/v1/app.py"
    github_repo_url = "https://github.com/110nard0/hngx_stage_1"
    status_code = 200

    return jsonify({
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': status_code
    }), 200
