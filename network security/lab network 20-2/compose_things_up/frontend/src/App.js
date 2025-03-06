import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';


const App = () => {

  const [flag, setFlag] = useState('Or maybe not?')

 
  React.useEffect(() => {
    fetch('http://localhost:8000/flag')
      .then(response => response.json())
      .then(data => setFlag(data.flag));
    console.log('flag', flag);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Here is your flag: {flag}
        </p>
      </header>
    </div>
  );
}

export default App;
