import React from 'react';
import './Footer.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub } from '@fortawesome/free-brands-svg-icons';

function App() {
  return (
    <div className="App">
      <div className="footer">
      <div className="github-logo">
          <a href="https://github.com/KUSUMAJOGARAO" target="_blank" rel="noopener noreferrer">
                <FontAwesomeIcon icon={faGithub} size="2x" color='black' />
          </a>

          </div>
      </div>
      <div className="footer1">
        <p>2023 @ Copyright Raj Reddy Center For Technology And Society. All Rights Reserved</p>
      </div>
    </div>
  );
}

export default App;