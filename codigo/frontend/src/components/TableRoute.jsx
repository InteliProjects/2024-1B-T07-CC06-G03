// Importa os hooks e componentes necessários do React e outras bibliotecas.
import React, { useState, useEffect } from "react";
import "./tableRoute.css"; // Importa o CSS para estilização do componente.
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"; // Importa o componente para utilizar ícones.
import { faArrowLeft, faArrowRight } from "@fortawesome/free-solid-svg-icons"; // Ícones usados para botões de navegação.
import Map from "./Map"; // Importa o componente Map personalizado.

// Define o componente TableRoute que recebe 'dia' e 'leiturista' como props.
const TableRoute = ({ dia, leiturista }) => {
  // Estado para a página atual inicializada em 1.
  const [currentPage, setCurrentPage] = useState(1);
  // Constante para definir o número de itens por página.
  const itemsPerPage = 10;
  // Estado para armazenar os dados filtrados.
  const [filteredData, setFilteredData] = useState([]);

  // Hook useEffect para buscar dados sempre que 'dia' ou 'leiturista' mudarem.
  useEffect(() => {
    setCurrentPage(1); // Reseta a página para 1 ao mudar os filtros.

    // Função assíncrona para buscar os dados do servidor.
    const fetchData = async () => {
      try {
        // Realiza a requisição HTTP e converte a resposta para JSON.
        const response = await fetch(
          `http://localhost:5000/routes/filter/${dia}/${leiturista}`
        );
        const data = await response.json();
        setFilteredData(data); // Atualiza o estado com os dados recebidos.
      } catch (error) {
        console.error("Erro ao buscar dados filtrados:", error);
      }
    };

    fetchData(); // Chama a função de busca de dados.
  }, [dia, leiturista]); // Dependências do useEffect.

  // Calcula os índices dos itens para a paginação.
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;

  // Função para atualizar a página atual.
  const paginate = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  // Extrai os itens para a página atual baseado nos índices calculados.
  const currentItems = filteredData.slice(indexOfFirstItem, indexOfLastItem);

  // Redutores para calcular totais de distância e tempo.
  const totalKm = filteredData.reduce(
    (total, current) => total + parseFloat(current.distancia),
    0
  );
  const totalTime = filteredData.reduce(
    (total, current) => total + parseInt(current.tempo.split(" ")[0]),
    0
  );

  // Calcula o total de páginas necessárias baseado no número de itens.
  const totalPages = Math.ceil(filteredData.length / itemsPerPage);

  // Função para renderizar botões de paginação dinamicamente.
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

  // Renderiza o componente JSX.
  return (
    <div className="table-container">
      <table className="data-table">
        <thead>
          <tr>
            <th>Index</th>
            <th>Origem</th>
            <th>Destino</th>
            <th>Tempo</th>
            <th>Distância Percorrida</th>
          </tr>
        </thead>
        <tbody>
          {currentItems.map((row, index) => (
            <tr key={index}>
              <td>{indexOfFirstItem + index + 1}</td>
              <td>{row.origem}</td>
              <td>{row.destino}</td>
              <td>{row.tempo}</td>
              <td>{row.distancia}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="totals-container">
        <div className="total-box">
          Kms Totais:{" "}
          <u>
            <strong>{totalKm.toFixed(2)} km</strong>
          </u>
        </div>
        <div className="total-box">
          Tempo Total:{" "}
          <u>
            <strong>{totalTime} minutos</strong>
          </u>
        </div>
      </div>
      <div className="empty-container-pag"></div>
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
      <Map routeData={filteredData} /> 
    </div>
  );
};

export default TableRoute;
