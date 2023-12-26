"use client";
import { ChatUI } from "@/components/ChatUI";
import GoogleMapComponent from "@/components/GoogleMapComponent";
import { useState, ChangeEvent, FormEvent } from "react";
import { SendHorizontal, Loader2 } from "lucide-react";
import { useRouter } from "next/navigation";

async function consumeStream(
  response: any,
  updateAiResponse: any,
  setError: any
) {
  const reader = response.body.getReader();
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) {
        break;
      }
      const textChunk = new TextDecoder("utf-8").decode(value);
      console.log("vtextChunk", textChunk);

      updateAiResponse(textChunk); // Update with each new chunk
    }
  } catch (error) {
    setError("Error while reading data from the stream.");
    console.error("Stream error:", error);
  }
}
interface ConversationEntry {
  sender: string;
  message: string;
}

interface MapState {
  center: { lat: number; lng: number };
  zoom: number;
  markers: Array<{ lat: number; lng: number; label: string }>;
}
export default function OpenAIChatBox() {
  const [inputValue, setInputValue] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [conversation, setConversation] = useState<ConversationEntry[]>([]);
  const [mapState, setMapState] = useState<MapState>({
    center: { lat: 16, lng: 40 },
    zoom: 16,
    markers: [],
  });
  const router = useRouter();

  const updateAiResponse = (newChunk: string) => {
    setConversation((prevConvo) => {
      const lastEntry = prevConvo.length
        ? prevConvo[prevConvo.length - 1]
        : null;
      if (lastEntry && lastEntry.sender === "AI") {
        return [
          ...prevConvo.slice(0, -1),
          { ...lastEntry, message: lastEntry.message + newChunk },
        ];
      }
      return [...prevConvo, { sender: "AI", message: newChunk }];
    });
  };

  const handleInputChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    setInputValue(e.target.value);
  };

  const updateMapState = async () => {
    try {
      const mapStateResponse = await fetch("/api/openai-map", {
        cache: "no-store",
      });
      if (mapStateResponse.status === 200) {
        const mapData = await mapStateResponse.json();
        // Transform the markers_state data into the expected format
        const markers = mapData.markers_state.latitudes.map(
          (lat: any, index: any) => ({
            lat: lat,
            lng: mapData.markers_state.longitudes[index],
            label: mapData.markers_state.labels[index],
          })
        );

        setMapState({
          center: {
            lat: mapData.map_state.latitude,
            lng: mapData.map_state.longitude,
          },
          zoom: mapData.map_state.zoom,
          markers: markers,
        });
        router.refresh();
      } else {
        console.error("Failed to fetch map state");
      }
    } catch (error) {
      console.error("Error fetching map state:", error);
    }
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!inputValue.trim()) return;

    setIsLoading(true);
    setError(null);
    setConversation([...conversation, { sender: "user", message: inputValue }]);

    try {
      const response = await fetch(
        `/api/streaming-openai?query=${inputValue}`,
        { cache: "no-store" }
      );
      if (!response.ok)
        throw new Error(`API request failed with status ${response.status}`);
      await consumeStream(response, updateAiResponse, setError);
      setInputValue("");
      router.refresh();
      await updateMapState();
    } catch (error: any) {
      setError("Error sending message: " + error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col-reverse md:flex-row min-h-[74vh] items-center justify-center">
      <div className="w-full md:w-1/2 h-full flex flex-col items-center justify-center m-2">
        <div className="overflow-y-auto max-h-[400px] h-full sm:max-h-[460px] md:max-h-[520px] lg:max-h-[570px] xl:max-h-[600px] w-full">
          {conversation.map((entry: any, index: any) => (
            <ChatUI key={index} sender={entry.sender} message={entry.message} />
          ))}
        </div>
        <form
          onSubmit={handleSubmit}
          className="relative w-full m-1 flex items-center justify-between space-x-2"
        >
          <textarea
            id="prompt"
            rows={1}
            className="mx-2 flex  disabled:cursor-not-allowed disabled:opacity-50 min-h-full w-full rounded-md border border-slate-300 bg-slate-200 p-2 text-base text-slate-900 placeholder-slate-400 focus:border-blue-600 focus:outline-none focus:ring-1 focus:ring-blue-600 "
            placeholder="Let's visit Japan!"
            value={inputValue}
            onChange={handleInputChange}
            disabled={isLoading}
          />
          <button
            type="submit"
            disabled={isLoading}
            className="absolute right-3 disabled:cursor-not-allowed disabled:opacity-50 rounded-r-lg py-[8px] text-sm  hover:text-blue-700 focus:outline-none focus:ring-4  border-slate-300  p-2 text-slate-700 placeholder-slate-400"
          >
            {isLoading ? (
              <Loader2 className="animate-spin" />
            ) : (
              <SendHorizontal />
            )}
            <span className="sr-only">Send message</span>
          </button>
        </form>
      </div>
      <div className="w-full h-[400px] sm:h-[460px] md:h-[520px] rounded-sm lg:h-[570px] xl:h-[600px] md:w-1/2 bg-gray-400 flex items-center justify-center m-4">
        <GoogleMapComponent
          center={mapState.center}
          zoom={mapState.zoom}
          markers={mapState.markers}
        />
      </div>
    </div>
  );
}
