import React from "react";
import { Button } from 'antd'


class Welcome extends React.Component {
	render() {
	    return (
				<div>
					<h3>Hello2, {this.props.name}</h3>
					<Button type="primary">Button</Button>
				</div>
			)
	  }
	}

const element = <Welcome name="YT" />

module.exports = Welcome;
module.exports.yt = element;
