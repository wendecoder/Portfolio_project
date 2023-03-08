// BiddingPage.js

import React, { useState, useEffect } from 'react';
import '../stylesheets/BiddingPage.css';

const BiddingPage = () => {
  const [timeRemaining, setTimeRemaining] = useState(60); // timer in seconds
  const [currentBid, setCurrentBid] = useState(100); // current bid
  const [bidPlaced, setBidPlaced] = useState(false); // whether a bid has been placed

  useEffect(() => {
    let timer;
    if (timeRemaining > 0) {
      timer = setTimeout(() => {
        setTimeRemaining(prevTime => prevTime - 1);
      }, 1000);
    } else {
      // end of bidding, do something
    }
    return () => clearTimeout(timer);
  }, [timeRemaining]);

  const handlePlaceBid = () => {
    // handle placing a bid
    setBidPlaced(true);
  };

  const handleCancelBid = () => {
    // handle canceling a bid
    setBidPlaced(false);
  };

  return (
    <div className="bidding-page-container">
      <div className="timer-container">
        <h3>Time Remaining: {timeRemaining}s</h3>
      </div>
      <div className="current-bid-container">
        <h3>Current Bid: {currentBid}</h3>
      </div>
      <div className="bid-actions-container">
        {!bidPlaced ? (
          <div className="place-bid-container">
            <button onClick={handlePlaceBid}>Place Bid</button>
          </div>
        ) : (
          <div className="cancel-bid-container">
            <button onClick={handleCancelBid}>Cancel Bid</button>
          </div>
        )}
      </div>
    </div>
  );
};

export default BiddingPage;
