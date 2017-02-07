import React, { Component } from 'react';
import { DatePicker } from 'antd';


class AntDate extends Component {
  render() {
    return (
      <div className="AntDate">
        <div className="AntDate-header">
          <h2>Antd DatePicker</h2>
        </div>
        <p>
          <div style={{margin: 10}}>
            <DatePicker />
          </div>
        </p>
      </div>
    );
  }
}

export default AntDate;
