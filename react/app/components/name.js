import React from "react";
class Welcome extends React.Component {
	render() {
	    return <h3>Hello, {this.props.name}</h3>;
	  }
	}

const element = <Welcome name="YT" />

module.exports = Welcome;
module.exports.yt = element;
