import React, { useState } from "react";
import {
  MapContainer,
  TileLayer,
  Polyline,
  Marker,
  Popup,
  Tooltip,
} from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "./map.css";
import icon from "leaflet/dist/images/marker-icon.png";
import iconShadow from "leaflet/dist/images/marker-shadow.png";

// Configuração do ícone padrão para os marcadores de origem.
const origemIcon = L.icon({
  iconUrl: icon,
  shadowUrl: iconShadow,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [16, -28],
});

// Configuração do ícone padrão para os marcadores de destino.
const destinoIcon = L.icon({
  iconUrl: icon,
  shadowUrl: iconShadow,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [1, -12],
});

// Componente funcional Map que aceita `routeData` como prop.
const Map = ({ routeData }) => {
  // Estado para controlar a visibilidade dos tooltips.
  const [showTooltip, setShowTooltip] = useState(false);

  // Verifica se os dados da rota estão vazios e retorna uma mensagem caso afirmativo.
  if (routeData.length === 0) {
    return <div>No route data available</div>;
  }

  // Prepara uma lista de posições geográficas dos pontos de origem e destino.
  const positions = [];
  routeData.forEach((point, index) => {
    positions.push([point.origem_latitude, point.origem_longitude]);
    positions.push([point.destino_latitude, point.destino_longitude]);
  });

  // Função para alternar a visibilidade dos tooltips.
  const toggleTooltip = () => {
    setShowTooltip(!showTooltip);
  };

  // Renderiza o container do mapa com marcadores e polilinhas.
  return (
    <div className="map-container">
      <button className="toggle-button" onClick={toggleTooltip}>
        {showTooltip ? "Remover index da rota" : "Mostrar index da rota"}
      </button>
      <MapContainer
        center={positions[0]}
        zoom={13}
        style={{ height: "400px", width: "100%" }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        {/* Marcadores para cada ponto de origem com popups associados. */}
        {routeData.map((point, index) => (
          <Marker
            key={`origem-${index}`}
            position={[point.origem_latitude, point.origem_longitude]}
            icon={origemIcon}
          >
            <Popup>{point.origem}</Popup>
          </Marker>
        ))}
        {/* Marcadores para cada ponto de destino com popups associados. */}
        {routeData.map((point, index) => (
          <Marker
            key={`destino-${index}`}
            position={[point.destino_latitude, point.destino_longitude]}
            icon={destinoIcon}
          >
            {showTooltip && (
              <Tooltip
                direction="top"
                offset={[0, -20]}
                opacity={1}
                permanent
                className="custom-tooltip"
              >
                {index + 1}
              </Tooltip>
            )}
            <Popup>{point.destino}</Popup>
          </Marker>
        ))}
        {/* Linhas conectando os pontos de origem e destino. */}
        <Polyline positions={positions} />
      </MapContainer>
    </div>
  );
};

export default Map;