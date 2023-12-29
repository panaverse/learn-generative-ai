"use client";

import { GoogleMap, MarkerF, useLoadScript } from "@react-google-maps/api";

interface GoogleMapComponentProps {
  center: { lat: number; lng: number };
  zoom: number;
  markers: Array<{ lat: number; lng: number; label: string }>;
}

const GoogleMapComponent:React.FC<GoogleMapComponentProps> = ({
  center,
  zoom,
  markers,
}) => {
  const { isLoaded, loadError } = useLoadScript({
    googleMapsApiKey: process.env.NEXT_PUBLIC_JS_GOOGLE_MAPS_KEY!,
    libraries: ["places"],
  });

  if (loadError) return <div>Error loading maps</div>;
  if (!isLoaded) return <div>Loading...</div>;

  return (
    <div className="h-[400px] sm:h-[460px] md:h-[520px] lg:h-[570px] xl:h-[600px] w-full">
      <GoogleMap
        zoom={zoom}
        center={center}
        mapContainerStyle={{ width: "100%", height: "100%" }}
      >
        {markers.map((marker, index) => (
          <MarkerF
            key={index}
            position={{ lat: marker.lat, lng: marker.lng }}
            label={marker.label}
          />
        ))}
      </GoogleMap>
    </div>
  );
};

export default GoogleMapComponent;
