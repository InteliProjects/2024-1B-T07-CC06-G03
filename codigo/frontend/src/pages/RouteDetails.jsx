import React from "react";
import { useParams, useNavigate, useLocation } from "react-router-dom";
import Sidebar from "../components/Sidebar";
import "../index.css";
import TableRoute from "../components/TableRoute";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowLeftLong } from '@fortawesome/free-solid-svg-icons';

// Definição do componente funcional RouteDetails
export default function RouteDetails() {
  // Utilização do hook useParams para obter os parâmetros da rota
  const { dia, leiturista } = useParams();
  
  // Utilização do hook useNavigate para navegação programática
  const navigate = useNavigate();
  
  // Utilização do hook useLocation para obter a localização atual
  const location = useLocation();

  // Função para navegar de volta para a página anterior
  const handleBack = () => {
    navigate(location.state.from);
  };

  // Renderização do componente
  return (
    <div>
      <Sidebar />
      <div className="content scrollable-content">
        <h1 className="title">Rotas de leitura de hidrômetros de consumo mensal</h1>
        <hr className="horizontal-line" />
        <div className="empty-container-route"></div>
        <h1 className="subtitle">Detalhes do dia {dia} - Leiturista {leiturista}</h1>
        <button className="back-button" onClick={handleBack}>
          <FontAwesomeIcon icon={faArrowLeftLong} />
        </button>
        <TableRoute dia={dia} leiturista={leiturista} />
      </div>
    </div>
  );
}
