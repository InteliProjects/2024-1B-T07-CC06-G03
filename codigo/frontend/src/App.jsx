// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Home from './pages/Home';
import Algorithm1 from './pages/Algorithm1';
import Algorithm2 from './pages/Algorithm2';
import RouteDetails from './pages/RouteDetails';

export default function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/algorithm1" element={<Algorithm1 />} />
          <Route path="/algorithm2" element={<Algorithm2 />} />
          <Route path="/route-details/:dia/:leiturista" element={<RouteDetails />} />
        </Routes>
      </div>
    </Router>
  );
}
