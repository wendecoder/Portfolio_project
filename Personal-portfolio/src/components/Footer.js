import { Container, Row, Col } from "react-bootstrap";
import logo from "../assets/img/logo1.svg";
import navIcon1 from '../assets/img/nav-icon1.svg';
import navIcon2 from '../assets/img/twit.svg';
import navIcon3 from '../assets/img/nav-icon3.svg';

export const Footer = () => {
  return (
    <footer className="footer">
      <Container>
        <Row className="align-items-center">
          <Col size={12} sm={6}>
          </Col>
          <Col size={12} sm={6} className="text-center text-sm-end">
            <div className="social-icon">
              <a href="https://www.linkedin.com/in/wendwossen-dufera"><img src={navIcon1} alt="linkedin" /></a>
              <a href="https://twitter.com/wende_dufera"><img src={navIcon2} alt="twitter" /></a>
              <a href="https://github.com/wendecoder"><img src={navIcon3} alt="github" /></a>
            </div>
            <p>Copyright 2023. All Rights Reserved</p>
          </Col>
        </Row>
      </Container>
    </footer>
  )
}
