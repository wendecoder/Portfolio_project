import React from 'react';
import { Col } from "react-bootstrap";
import './Button.css';
export const DownloadButton = () => {
  return (
    <Col size={12} sm={6} md={10}>
      <div className="downloadbutton">
        <h2>Check out my resume by clicking the button below!</h2>
        <a href='https://drive.google.com/file/d/1Hy7EJO4n3GdQuKhHmdkZ4tAoxKYXPBAf/view?usp=share_link'> <button className="button">
        Watch Resume
        </button>
        </a>
      </div>
    </Col>
  );
}


