import React, { Component } from 'react';
//import logo from './logo.svg';
import logo from './assets/logo.png'
//import './App.css';
import AntdDemo from './demo/antd/Demo'


class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <AntdDemo />
      </div>
    );
  }
}

export default App;
