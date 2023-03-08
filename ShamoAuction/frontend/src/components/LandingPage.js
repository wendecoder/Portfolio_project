import React, { useState } from 'react';
import backgroundImage from '../stylesheets/background.jpg';
import '../stylesheets/LandingPage.css';
import { FaHome, FaCar, FaGem, FaBoxes } from 'react-icons/fa';


function LandingPage(props) {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');


  const handleLogin = async () => {

    const info = { email1: email, password1: password };
    const response = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(info)
    });
    const data = await response.json();
    if (data.success) {
      const userId = data.userId; // assuming the response contains the user ID
      props.history.push(`/user/${userId}`);
    } else {
    // handle login failure
    alert(data.message)
    }
};

  const handleSignup = (event) => {
    // Handle signup logic here
    event.preventDefault();


    const data = { email1: email, password1: password };
    const options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    };

    fetch('/signup', options)
      .then(response => {
        if (response.ok) {
          // Signup was successful
          alert('Signup successful!');
        } else {
          // Signup failed
          alert('Signup failed.');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  return (
    <div className="landing-page">
      <div className="background-image" style={{ backgroundImage: `url(${backgroundImage})` }} />
      <div className="content">
	<div className="description">
          <h1>Welcome to SHAMO Auctioning Site</h1>
	  <p>Our site provides a variety of auction services, including:</p>
          <ul className="services-list">
            <li>
              <FaHome className="service-icon" />
              Real estate auctions
            </li>
            <li>
              <FaCar className="service-icon" />
              Automotive auctions
            </li>
            <li>
              <FaGem className="service-icon" />
              Jewelry and fine art auctions
            </li>
            <li>
              <FaBoxes className="service-icon" />
              General merchandise auctions
            </li>
          </ul>
          <p>Sign up today to start bidding on your favorite items!</p>
	</div>
	<div className="login-form">
          {isLogin ? (
          <div>
            <h2>Login</h2>
            <form>
              <label htmlFor="email">Email or User Name</label>
              <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
              <br />
              <label htmlFor="password">Password</label>
              <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
              <br />
              <button type="button" onClick={handleLogin}>Login</button>
            </form>
            <p>Don't have an account? <button type="button" onClick={() => setIsLogin(false)}>Sign up</button></p>
          </div>
        ) : (
          <div>
            <h2>Sign Up</h2>
            <form>
              <label htmlFor="email">Email or User Name</label>
              <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
              <br />
              <label htmlFor="password">Password</label>
              <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
              <br />
              <button type="button" onClick={handleSignup}>Sign up</button>
            </form>
            <p>Already have an account? <button type="button" onClick={() => setIsLogin(true)}>Login</button></p>
          </div>
        )}
	</div>
      </div>
    </div>
  );
}

export default LandingPage;
