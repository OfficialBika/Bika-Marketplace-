from datetime import datetime

async def complete_order(db, order_id:str):
    result = await db.marketplace_orders.update_one(
        {"_id": order_id},
        {"$set":{"status":"completed","updated_at":datetime.utcnow()}}
    )
    return {"success": result.modified_count > 0}
