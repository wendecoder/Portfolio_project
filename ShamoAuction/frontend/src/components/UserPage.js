import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';
import '../stylesheets/UserPage.css';

const UserPage = (props) => {
  const [items, setItems] = useState([]);
  const history = useHistory();

  useEffect(() => {
    const fetchItems = async () => {
      try {
	const userId = props.match.params.userId;
        const response = await axios.get(`http://localhost:5000/users/${userId}/items`);
        setItems(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchItems();
  }, [props.match.params.userId]);

  const handleFeedbackClick = () => {
    // TODO: handle feedback button click
  };

  const handleListItemClick = () => {
    // TODO: handle list item button click
    history.push('/listitem');
  };

  const handleBidClick = () => {
    // TODO: handle bid on item button click
    history.push('/letsbid');
  };

  const handleLogoutClick = () => {
    // TODO: handle logout button click
    history.push('/');
  };

  return (
    <div className="user-page">
      <div className="header">
        <h1>Welcome to Your User Page</h1>
        <button className="logout-btn" onClick={handleLogoutClick}>Logout</button>
      </div>
      <div className="content">
        <div className="item-list">
          <h2>Your Listed Items</h2>
          <ul>
            {items.map(item => (
              <li key={item.id}>
                <div className="item-image" style={{ backgroundImage: `url(${item.image})` }}></div>
                <div className="item-details">
                  <h3>{item.name}</h3>
                  <p>{item.description}</p>
                  <p>Current Bid: {item.currentBid}</p>
                </div>
              </li>
            ))}
          </ul>
        </div>
        <div className="actions">
          <button className="feedback-btn" onClick={handleFeedbackClick}>Feedback</button>
          <button className="listitem-btn" onClick={handleListItemClick}>List an Item</button>
          <button className="bid-btn" onClick={handleBidClick}>Bid on an Item</button>
        </div>
      </div>
    </div>
  );
};

export default UserPage;
