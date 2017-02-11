import React from 'react'
import ReactDOM from 'react-dom'
import AntdDemo from './antd/Demo'
//import AntDemo from './antd/index'


function formatDate(date) {
      return date.toLocaleDateString();
    }

/*
function AntDemo(){
	return (
		<p>
			<div style={{margin: 10}}>
				<DatePicker />
			</div>
			<Button type="primary">Button</Button>
		</p>
	)
}
*/

function Avatar(props) {
  return (
    <img className="Avatar"
      src={props.user.avatarUrl}
      alt={props.user.name}
    />
  );
}

function UserInfo(props) {
  return (
    <div className="UserInfo">
      <Avatar user={props.user} />
      <div className="UserInfo-name">
        {props.user.name}
				<AntdDemo />
      </div>
    </div>
  );
}

function Comment(props) {
  return (
    <div className="Comment">
      <UserInfo user={props.author} />
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}

const comment = {
      date: new Date(),
      text: 'I hope you enjoy learning React!',
      author: {
        name: 'Hello Kitty',
        avatarUrl: 'http://localhost:8000/static/logo.png'
      }
    };

ReactDOM.render(
      <Comment
        date={comment.date}
        text={comment.text}
        author={comment.author} />,
      document.getElementById('root')
    );
