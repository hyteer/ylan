import React, { Component } from 'react';
import { Button,DatePicker } from 'antd';

class Demo extends Component {
  render() {
    return (
			<div class="antddemo">
				<h3>Antd React Demo</h3>
			<p>
				<div style={{margin: 10}}>
					<DatePicker />
				</div>
				<Button type="primary">Button</Button>
			</p>
		</div>
    );
  }
}

export default Demo;
