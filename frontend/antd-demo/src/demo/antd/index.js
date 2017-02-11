import React from 'react'
import { Button,DatePicker } from 'antd';

const AntdDemo = function AntDemo(){
	return (
		<p>
			<div style={{margin: 10}}>
				<DatePicker />
			</div>
			<Button type="primary">Button</Button>
		</p>
	)
}

export default AntdDemo
