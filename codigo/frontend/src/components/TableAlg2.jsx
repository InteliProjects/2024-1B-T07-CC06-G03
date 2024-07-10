import React, { useState, useEffect } from "react";
import "./table.css"; // Importa o CSS para estilizar o componente.
import { useNavigate } from "react-router-dom"; // Hook para navegação entre rotas.
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"; // Componente para usar ícones.
import { faArrowLeft, faArrowRight, faChevronRight } from "@fortawesome/free-solid-svg-icons"; // Ícones de seta para a navegação.

// Componente funcional TableAlg2 com props de entrada.
const TableAlg2 = ({
  selectedDia,
  selectedLeiturista,
  selectedAlerta,
  data,
  executionTime,
  numeroIteracoes,
}) => {
  const [currentPage, setCurrentPage] = useState(1); // Estado para controlar a página atual.
  const [hoveredDia, setHoveredDia] = useState(null); // Estado para controlar a exibição da mensagem.
  const itemsPerPage = 10; // Número fixo de itens por página.
  const navigate = useNavigate(); // Hook para realizar navegação programática.

  // Efeito para reiniciar a página para 1 sempre que os filtros mudam.
  useEffect(() => {
    setCurrentPage(1);
  }, [selectedDia, selectedLeiturista, selectedAlerta]);

  // Cálculo para índices dos itens na página atual.
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;

  // Função para mudar a página atual.
  const paginate = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  // Filtragem dos dados com base nos critérios selecionados pelo usuário.
  const filteredData = data.filter((row) => {
    if (selectedDia && row.dia !== selectedDia) return false;
    if (selectedLeiturista && row.leiturista !== selectedLeiturista)
      return false;
    if (selectedAlerta && row.alerta !== selectedAlerta) return false;
    return true;
  });

  // Itens da página atual.
  const currentItems = filteredData.slice(indexOfFirstItem, indexOfLastItem);

  // Função para navegar para detalhes da rota.
  const handleRotaClick = (dia, leiturista) => {
    navigate(`/route-details/${dia}/${leiturista}`, {
      state: { from: "/algorithm2" },
    });
  };

  // Cálculo do total de páginas.
  const totalPages = Math.ceil(filteredData.length / itemsPerPage);

  // Renderização dos botões de paginação.
  const renderPaginationButtons = () => {
    const buttons = [];
    let startPage = Math.max(1, currentPage);
    let endPage = Math.min(totalPages, startPage + 2);

    if (currentPage > 1) {
      buttons.push(
        <button
          key="1"
          onClick={() => paginate(1)}
          className="pagination-button"
        >
          1
        </button>,
        <button key="ellipsis-left" disabled className="pagination-ellipsis">
          ...
        </button>
      );
    }

    for (let i = startPage; i <= endPage; i++) {
      buttons.push(
        <button
          key={i}
          onClick={() => paginate(i)}
          className={`pagination-button ${i === currentPage ? "active" : ""}`}
        >
          {i}
        </button>
      );
    }

    if (endPage < totalPages) {
      buttons.push(
        <button key="ellipsis-right" disabled className="pagination-ellipsis">
          ...
        </button>
      );
    }

    return buttons;
  };

  // Função para calcular iterações totais baseadas na última rota e número de iterações.
  const lastRouteNumber = () => {
    if (filteredData.length > 0) {
      const lastRoute = filteredData[filteredData.length - 1].rota;
      const lastNumber = parseInt(lastRoute.split(" ")[1]); // Assume que o número da rota está no formato 'Rota x'.
      return lastNumber;
    } else {
      return 0;
    }
  };

  const totalIterations = () => {
    const lastRoute = lastRouteNumber();
    return lastRoute * numeroIteracoes; // Calcula iterações totais.
  };

  // Estrutura do JSX retornado pelo componente.
  return (
    <div className="table-container">
      <table className="data-table">
        <thead>
          <tr>
            <th>Rota</th>
            <th>Tempo Utilizado</th>
            <th>Dia</th>
            <th>Distância Percorrida</th>
            <th>Leiturista</th>
            <th>Alerta</th>
          </tr>
        </thead>
        <tbody>
          {currentItems.map((row, index) => (
           <tr key={index}>
           <td>{row.rota}</td>
           <td>{row.tempo}</td>
           <td
                className="rota-cell"
                onClick={() => handleRotaClick(row.dia, row.leiturista)}
                onMouseEnter={() => setHoveredDia(index)}
                onMouseLeave={() => setHoveredDia(null)}
              >
                <div className="dia-content">
                  <span className="dia-text">{row.dia}</span>
                  <FontAwesomeIcon icon={faChevronRight} className="chevron-icon" />
                </div>
                {hoveredDia === index && (
                  <div className="tooltip">Visualizar detalhe da rota</div>
                )}
              </td>
           <td>{row.distancia}</td>
           <td>{row.leiturista}</td>
           <td className={`alerta ${row.alerta}`}>{row.alerta}</td>
         </tr>
          ))}
        </tbody>
      </table>
      <div className="totals-container">
        <div className="total-box">
          SubRotas Totais:{" "}
          <u>
            <strong>{filteredData.length}</strong>
          </u>
        </div>
        <div className="total-box">
          Tempo de Execução:{" "}
          <u>
            <strong>{executionTime}</strong>
          </u>
        </div>
        <div className="total-box">
          Número de Iterações:{" "}
          <u>
            <strong>{totalIterations()}</strong>
          </u>
        </div>
      </div>
      <div className="pagination">
        <button
          onClick={() => paginate(currentPage - 1)}
          disabled={currentPage === 1}
          className="pagination-arrow"
        >
          <FontAwesomeIcon icon={faArrowLeft} />
        </button>
        {renderPaginationButtons()}
        <button
          onClick={() => paginate(currentPage + 1)}
          disabled={indexOfLastItem >= filteredData.length}
          className="pagination-arrow"
        >
          <FontAwesomeIcon icon={faArrowRight} />
        </button>
      </div>
    </div>
  );
};

export default TableAlg2;
