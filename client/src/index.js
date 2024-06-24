import React from "react";
import App from "./components/App";
import "./index.css";
import ReactDOM from "react-dom/client";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// const container = document.getElementById("root");
// const root = createRoot(container);
// root.render(<App />);
