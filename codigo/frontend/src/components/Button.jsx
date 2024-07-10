import React from "react";
import "./button.css";

// Define um componente funcional chamado 'Button'. Este componente aceita props: `text`, `iconSrc`, e `onClick`.
const Button = ({ text, iconSrc, onClick }) => {
  // Retorna um elemento JSX que representa um botão.
  return (
    <button onClick={onClick} className="custom-button">
      {/* 
              Verifica se `iconSrc` está presente. Se estiver, renderiza um elemento <img>
              com o atributo `src` definido por `iconSrc` e uma classe para estilização. 
              O `alt` é definido como "Icon" para acessibilidade.
            */}
      {iconSrc && <img src={iconSrc} alt="Icon" className="button-icon" />}
      {/* Renderiza o texto passado via prop `text` dentro do botão. */}
      {text}
    </button>
  );
};

// Exporta o componente 'Button' para que possa ser importado e usado em outros arquivos.
export default Button;
