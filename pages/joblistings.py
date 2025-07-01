from flask import Blueprint, render_template, request



jobListing_bp = Blueprint("joblistings", __name__)


@jobListing_bp.route("/search")
def search_results():
    title = request.args.get("title", "all")
    location = request.args.get("location", "all")
    site = request.args.get("site", "all")

    query = f"{title} jobs in {location} via {site}"





