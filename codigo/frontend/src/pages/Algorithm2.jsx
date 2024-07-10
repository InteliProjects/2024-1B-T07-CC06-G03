import React, { useState, useEffect } from "react";
import Sidebar from "../components/Sidebar";
import TableAlg2 from "../components/TableAlg2";
import "../index.css"; 
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faShare, faTimes, faDownload } from "@fortawesome/free-solid-svg-icons";
import axios from 'axios';
import { saveAs } from 'file-saver';

// Definição do componente funcional Algorithm2
export default function Algorithm2() {
  // Declaração de estados usando o hook useState
  const [selectedDia, setSelectedDia] = useState("");
  const [selectedLeiturista, setSelectedLeiturista] = useState("");
  const [selectedAlerta, setSelectedAlerta] = useState("");
  const [numeroDias, setNumeroDias] = useState("");
  const [tempoLeitura, setTempoLeitura] = useState("");
  const [horasTrabalho, setHorasTrabalho] = useState("");
  const [loading, setLoading] = useState(false);
  const [simulationFinished, setSimulationFinished] = useState(false);
  const [data, setData] = useState([]);
  const [executionTime, setExecutionTime] = useState(null);
  const [numeroIteracoes, setNumeroIteracoes] = useState(NaN);
  const [errorMessage, setErrorMessage] = useState("");
  const [showDownloadButton, setShowDownloadButton] = useState(false);

  // Efeito colateral para recuperar dados do localStorage quando o componente é montado
  useEffect(() => {
    const savedData = localStorage.getItem('algorithm2Data');
    const savedExecutionTime = localStorage.getItem('algorithm2ExecutionTime');
    const savedNumeroIteracoes = localStorage.getItem('algorithm2NumeroIteracoes');
    if (savedData) {
      setData(JSON.parse(savedData));
      setSimulationFinished(true);
      setShowDownloadButton(true);
    }
    if (savedExecutionTime) {
      setExecutionTime(savedExecutionTime);
    }
    if (savedNumeroIteracoes) {
      setNumeroIteracoes(parseInt(savedNumeroIteracoes, 10));
    }
  }, []);

  // Função para iniciar a automação quando o botão "Enviar" é clicado
  const handleEnviar = async () => {
     // Verificação se todos os parâmetros estão preenchidos
     if (!numeroDias || !tempoLeitura || !horasTrabalho) {
      setErrorMessage("Preencha todos os parâmetros para iniciar a automação");
      return;
    }

    setErrorMessage("")
    setLoading(true);
    setSimulationFinished(false);

    const params = {
      select_algo: 1,
      time_readings: parseInt(tempoLeitura, 10),
      hours_work: parseInt(horasTrabalho, 10),
      total_days: parseInt(numeroDias, 10)
    };

    try {
      await axios.post("http://localhost:5000/start_automation", params);
      checkSimulationStatus();
    } catch (error) {
      console.error("Erro ao iniciar a automação:", error);
      setLoading(false);
    }
  };

  // Função para resetar a automação quando o botão "Resetar" é clicado
  const handleReset = async () => {
    try {
      await axios.get("http://localhost:5000/reset_automation");
      setLoading(false);
      setSimulationFinished(false);
      setData([]);
      setNumeroDias("");
      setTempoLeitura("");
      setHorasTrabalho("");
      setExecutionTime(null);
      setNumeroIteracoes(NaN);
      setErrorMessage("");
      setShowDownloadButton(false);
      localStorage.removeItem('algorithm2Data');
      localStorage.removeItem('algorithm2ExecutionTime');
      localStorage.removeItem('algorithm2NumeroIteracoes');
    } catch (error) {
      console.error("Erro ao resetar a automação:", error);
    }
  };

  // Função para verificar o status da automação periodicamente
  const checkSimulationStatus = async () => {
    const intervalId = setInterval(async () => {
      try {
        const response = await axios.get("http://localhost:5000/automation_status");
        if (response.data.state === "finished") {
          clearInterval(intervalId);
          const executionTimeInMinutes = response.data.result;
          const hours = Math.floor(executionTimeInMinutes / 60);
          const minutes = (executionTimeInMinutes % 60).toFixed(0);
          const formattedExecutionTime = `${hours} hora${hours !== 1 ? 's' : ''} e ${minutes} minuto${minutes !== 1 ? 's' : ''}`;
          setExecutionTime(formattedExecutionTime);
          localStorage.setItem('algorithm2ExecutionTime', formattedExecutionTime);
          fetchSimulationResults();
        }
      } catch (error) {
        console.error("Erro ao verificar o status da automação:", error);
        clearInterval(intervalId);
        setLoading(false);
      }
    }, 2000);
  };

  // Função para buscar os resultados da automação após a conclusão
  const fetchSimulationResults = async () => {
    try {
      const response = await axios.get("http://localhost:5000/summary-data");
      setData(response.data);
      setSimulationFinished(true);
      setLoading(false);
      setShowDownloadButton(true);
      const iteracoes = parseInt(numeroDias, 10);
      setNumeroIteracoes(iteracoes);
      localStorage.setItem('algorithm2Data', JSON.stringify(response.data));
      localStorage.setItem('algorithm2NumeroIteracoes', iteracoes);
    } catch (error) {
      console.error("Erro ao buscar os resultados da automação:", error);
      setLoading(false);
    }
  };

  // Função para lidar com o clique no botão de download
  const handleDownload = async () => {
    try {
      const detailedDataResponse = await axios.get("http://localhost:5000/download/detailed-data", { responseType: 'blob' });
      const summaryDataResponse = await axios.get("http://localhost:5000/download/summary-data", { responseType: 'blob' });

      const detailedDataBlob = new Blob([detailedDataResponse.data], { type: 'text/csv;charset=utf-8;' });
      const summaryDataBlob = new Blob([summaryDataResponse.data], { type: 'text/csv;charset=utf-8;' });

      saveAs(detailedDataBlob, 'detailed-data-automation.csv');
      saveAs(summaryDataBlob, 'summary-data-automation.csv');
    } catch (error) {
      console.error("Erro ao fazer o download dos dados:", error);
    }
  };

  // Renderização do componente
  return (
    <div>
      <Sidebar />
      <div className="content scrollable-content">
        <h1 className="title">Rotas de leitura de hidrômetros de consumo mensal</h1>
        <hr className="horizontal-line" />
        <div className="input-container">
          <div className="input-filters-container">
            <input type="number" id="numeroDias" name="numeroDias" className="large-input" placeholder="Número de dias" value={numeroDias} onChange={(e) => setNumeroDias(e.target.value)} />
            <input type="number" id="tempoLeitura" name="tempoLeitura" className="large-input" placeholder="Tempo de leitura (min)" value={tempoLeitura} onChange={(e) => setTempoLeitura(e.target.value)} />
            <input type="number" id="horasTrabalho" name="horasTrabalho" className="large-input" placeholder="Horas de trabalho" value={horasTrabalho} onChange={(e) => setHorasTrabalho(e.target.value)} />
            <button onClick={handleEnviar} className="send-button">
              <FontAwesomeIcon icon={faShare} />
            </button>
            <button onClick={handleReset} className="reset-button">
              <FontAwesomeIcon icon={faTimes} />
            </button>
            {showDownloadButton && (
              <button onClick={handleDownload} className="download-button" title="Download resultados gerados">
                <FontAwesomeIcon icon={faDownload} />
              </button>
            )}
          </div>
        </div>
        <div className="filters-container">
          <div className="filter">
            <select id="dia" name="dia" className="dropdown-dia" value={selectedDia} onChange={(e) => setSelectedDia(e.target.value)}>
              <option value="">Dia</option>
              {Array.from({ length: 22 }, (_, i) => (
                <option key={i + 1} value={i + 1}>
                  {i + 1}
                </option>
              ))}
            </select>
          </div>
          <div className="filter">
            <select id="leiturista" name="leiturista" className="dropdown-leiturista" value={selectedLeiturista} onChange={(e) => setSelectedLeiturista(e.target.value)}>
              <option value="">Leiturista</option>
              {Array.from({ length: 58 }, (_, i) => (
                <option key={i + 1} value={i + 1}>
                  {i + 1}
                </option>
              ))}
            </select>
          </div>
          <div className="filter">
            <select id="alerta" name="alerta" className="dropdown-alerta" value={selectedAlerta} onChange={(e) => setSelectedAlerta(e.target.value)}>
              <option value="">Alerta</option>
              <option value="Ok">Ok</option>
              <option value="Excedido">Excedido</option>
              <option value="Insuficiente">Insuficiente</option>
            </select>
          </div>
        </div>
        {errorMessage && (
          <div className="error-message">
            {errorMessage}
          </div>
        )}
        {loading ? (
          <div className="loading-container">
            <div className="loading-spinner"></div>
            <p>Aguardando a finalização da automação...</p>
          </div>
        ) : simulationFinished ? (
          <TableAlg2 data={data} selectedDia={selectedDia} selectedLeiturista={selectedLeiturista} selectedAlerta={selectedAlerta} executionTime={executionTime} numeroIteracoes={numeroIteracoes} />
        ) : (
          <div className="message-container">
            <p>Insira os parâmetros solicitados nos campos acima.</p>
          </div>
        )}
      </div>
    </div>
  );
}
