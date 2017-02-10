import React, { Component } from 'react';
//import { Button } from 'antd';
import './App.css';
import AntdDemo from './demo/antd/index'

class App extends Component {
  render() {
    return (
      <div className="App">
          <h3>Demo Home</h3>
          <AntdDemo />
      </div>
    );
  }
}

export default App;
