import React from "react";
import ReactDOM from "react-dom";
import Name from "./components/name.js";
import nm from "./components/name.js";
import User from "./components/user.js"
var Name2 = require('./components/name.js');  // 导入模块的另一种方法
import TopicHeader from './components/header'

ReactDOM.render(
	<TopicHeader name="A Test Topic" />,
	document.getElementById('header')
);

ReactDOM.render(
  <Name name="Silly" />,  //nm.yt,
  document.getElementById('root')
);
ReactDOM.render(
  <Name name="YT" />,  //nm.yt,
  document.getElementById('example')
);
ReactDOM.render(
  <User />,  //nm.yt,
  document.getElementById('user')
);
console.log("main app has been loaded...");
