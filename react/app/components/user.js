import React from "react";


var user = {
  firstName: "YT",
  lastName: "Hoo",
  isLoggedIn: false
};

/**************** functions **************/
function formatName(user){
  return user.firstName + " " + user.lastName;
}

function UserGreeting(props) {
  return <h3>Welcome back!</h3>;
}

function GuestGreeting(props) {
  return <h3>Please sign up.</h3>;
}

function LoginButton(props) {
  return (
    <button onClick={props.onClick}>
      Login
    </button>
  );
}

function LogoutButton(props) {
  return (
    <button onClick={props.onClick}>
      Logout
    </button>
  );
}

/******************* condition ****************/
function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
    if (isLoggedIn) {
      return <UserGreeting />;
    }
  return <GuestGreeting />;
}
const greet = <div>{Greeting(user)}</div>

/****************** LoginControl ***************/
class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
    this.state = {isLoggedIn: false};
  }

  handleLoginClick() {
    this.setState({isLoggedIn: true});
  }

  handleLogoutClick() {
    this.setState({isLoggedIn: false});
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;

    let button = null;
    if (isLoggedIn) {
      button = <LogoutButton onClick={this.handleLogoutClick} />;
    } else {
      button = <LoginButton onClick={this.handleLoginClick} />;
    }

    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn} />
        {button}
      </div>
    );
  }
}
module.exports = LoginControl;
