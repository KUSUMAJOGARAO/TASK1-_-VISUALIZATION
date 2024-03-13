//App.js
import React from "react";
import Header from "../Components/Header/Header";
import Plot from "../Components/Plot/Plot";
import Footer from "../Components/Footer/Footer";
import "./main.css";

function App() {
  return (
    <div className="App">
      <Header />
      <Plot />
      <Footer />
    </div>
  );
}

export default App;