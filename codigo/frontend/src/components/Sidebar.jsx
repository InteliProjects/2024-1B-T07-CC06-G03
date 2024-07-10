import React, { useState } from "react";
import "./sidebar.css";
import "../index.css";
import egeuLogo from "../assets/e6euLogo.png";
import { Link, useLocation } from "react-router-dom";

// Define o componente funcional Sidebar.
const Sidebar = () => {
  // Utiliza o hook useLocation para obter a localização atual da rota.
  const location = useLocation();
  // Define um estado para rastrear o algoritmo ativo, inicializando com o caminho atual da rota.
  const [activeAlgorithm, setActiveAlgorithm] = useState(location.pathname);

  // Define uma função para manipular cliques nos itens do menu, atualizando o estado do algoritmo ativo.
  const handleAlgorithmClick = (algorithm) => {
    setActiveAlgorithm(algorithm);
  };

  // Renderiza a barra lateral com a logo e os links de navegação.
  return (
    <div className="sidebar">
      <div className="logo-container">
        <img src={egeuLogo} alt="EGEU Logo" className="logo" />
      </div>
      <div className="menu-items">
        {/* Links que navegam para diferentes algoritmos. O className é condicional para destacar o item ativo. */}
        <Link
          to="/algorithm1"
          className={activeAlgorithm === "/algorithm1" ? "active" : ""}
          onClick={() => handleAlgorithmClick("/algorithm1")}
        >
          Roteirização Simulada
        </Link>
        <Link
          to="/algorithm2"
          className={activeAlgorithm === "/algorithm2" ? "active" : ""}
          onClick={() => handleAlgorithmClick("/algorithm2")}
        >
          Roteirização Automatizada
        </Link>
      </div>
    </div>
  );
};

// Exporta o componente Sidebar para que possa ser usado em outras partes da aplicação.
export default Sidebar;
