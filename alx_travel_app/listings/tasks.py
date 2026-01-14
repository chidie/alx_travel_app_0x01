from alx_travel_app.celery import app as celery_app


@celery_app.task
def heavy_processing_task(listing_id):
    return {"id": listing_id, "status": "processed"}