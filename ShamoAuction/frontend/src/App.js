import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import './stylesheets/App.css';
import LandingPage from './components/LandingPage';
import UserPage from './components/UserPage';
import ListItem from './components/ListItem';
import BiddingPage from './components/BiddingPage';

function App() {
    return (
      <div className="App">
	<Router>
          <Switch>
            <Route path='/' exact component={LandingPage} />
            <Route exact path='/user/:userId' component={UserPage} />
            <Route exact path='/letsbid' component={BiddingPage} />
            <Route exact path='/listitem' component={ListItem} />
          </Switch>
        </Router>
      </div>
    );
}

export default App;
