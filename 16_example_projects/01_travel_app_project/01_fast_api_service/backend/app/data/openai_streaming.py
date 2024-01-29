# data layer
import shelve
from typing import Optional, Any
from pydantic import ValidationError

from ..models.openai_streaming import MapState, MarkersState

# Seed Prompt
BASE_PROMPT: str = """You are an AI Travel Assistant who make global travellers traval planning fun and interactive:

Before replying perform the following steps:

1. If user share any travel location name, update the map to go to that place and Add markers on the place.
2. if user shared any travel suggestions update them map.

If user sends any general message share with them you are a helpful AI Travel Assistant and you can help them with travel planning.

"""

# Initial map state with class instances
ai_powered_map: dict[str, Any] = {
    "map_state": MapState(latitude=39.949610, longitude=75.150282, zoom=16).model_dump(),
    "markers_state": MarkersState(latitudes=[], longitudes=[], labels=[]).model_dump()
}

# Function to update map and markers
def update_map_and_markers(
    map_state: Optional[MapState] = None,
    markers_state: Optional[MarkersState] = None
) -> dict[str, Any]:

    response_format = {"status": "", "values": ai_powered_map}
    try:
        if map_state is not None:
            ai_powered_map["map_state"] = map_state.model_dump()

        if markers_state is not None:
            ai_powered_map["markers_state"] = markers_state.model_dump()

        response_format["status"] = "Map location and markers updated Now continue answering my last question"

    except ValidationError as e:
        response_format["status"] = f"Error update map: {
            e}, continue answering my last question"

    return response_format


# data layer to manage chat_history
class Database:
    def __init__(self, dbName: str = "chat_history") -> None:
        self.dbName = dbName

    # Load chat history from shelve file
    def load_chat_history(self) -> [dict]:
        with shelve.open(self.dbName) as db:
            return db.get("messages", [{"role": "system", "content": BASE_PROMPT}])

    # Save chat history to shelve file

    def save_chat_history(self, messages: [dict]):
        print("Database: Save", messages)
        with shelve.open(self.dbName) as db:
            db["messages"] = messages
