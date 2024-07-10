import React, { useRef, useState } from "react";
import axios from "axios";
import "../index.css";
import { useNavigate } from 'react-router-dom';
import Button from "../components/Button";
import logoAegea from "../assets/aegeaLogo.png";
import logoADR from "../assets/adrLogo.png";
import egeuLogo from "../assets/e6euLogo.png";
import iconUpload from "../assets/iconUpload.png";

// Definição do componente funcional Home
export default function Home() {
  // Declaração do hook useNavigate para navegação de rotas
  const navigate = useNavigate();
  
  // Declaração de referências e estados usando hooks useRef e useState
  const fileInputRef = useRef(null);
  const [errorMessage, setErrorMessage] = useState("");

  // Função para abrir o seletor de arquivos quando o botão é clicado
  const handleCsvUploadClick = () => {
    fileInputRef.current.click();
  };

  // Função para tratar a mudança de arquivo selecionado
  const handleFileChange = async (event) => {
    const file = event.target.files[0];

    if (file) {
      const formData = new FormData();
      formData.append("file", file);
      try {
        const response = await axios.post('http://localhost:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        if (response.status === 200) {
          navigate("/algorithm1");
        } else {
          setErrorMessage(`Erro ao fazer upload do arquivo: ${response.statusText}`);
        }
      } catch (error) {
        if (error.response && error.response.data && error.response.data.erro) {
          setErrorMessage(`Erro ao fazer upload do arquivo: ${error.response.data.erro}`);
        } else {
          setErrorMessage(`Erro ao fazer upload do arquivo: ${error.message}`);
        }
      }
    }
  };

  // Renderização do componente
  return (
    <div className="home-container">
      <div className="left-side">
        <div className="logo-top-left">
          <img src={logoAegea} alt="Logo" />
        </div>
        <div className="text-icon-bottom-left">
          <p>
            Bem-vindo ao E6eu!<br />
            A solução de otimização de rotas da Aegea
          </p>
        </div>
      </div>
      <div className="right-side">
        <img className="egeuLogo" src={egeuLogo} alt="E6EU Logo" />
        <div className="input-button">
          <input
            type="file"
            accept=".csv"
            ref={fileInputRef}
            style={{ display: "none" }}
            onChange={handleFileChange}
          />
          <Button
            text="Insira o CSV"
            iconSrc={iconUpload}
            onClick={handleCsvUploadClick}
          />
        </div>
        {errorMessage && (
          <div className="error-message">
            {errorMessage}
          </div>
        )}
      </div>
    </div>
  );
}