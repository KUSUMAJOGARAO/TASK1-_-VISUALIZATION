// components/header/header.js
import React from 'react';
import './Header.css';

function Header() {
  return (
    <header className="header">
      <nav className="navbar">
        <div className="logo">
          <h1>K-Hub React Practice App</h1>
        </div>
      </nav>
    </header>
  );
}

export default Header;