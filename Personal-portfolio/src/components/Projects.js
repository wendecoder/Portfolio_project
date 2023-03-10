import { Container, Row, Col, Tab, Nav } from "react-bootstrap";
import { ProjectCard } from "./ProjectCard";
import { DownloadButton } from "./DownloadResume";
import projImg1 from "../assets/img/projimg1.png";
import projImg2 from "../assets/img/projimg2.png";
import projImg3 from "../assets/img/projimg3.png";
import projImg4 from "../assets/img/projimg4.png";
import projImg5 from "../assets/img/projimg5.jpg";
import projImg6 from "../assets/img/projimg6.png";
import colorSharp2 from "../assets/img/color-sharp2.png";
import 'animate.css';
import TrackVisibility from 'react-on-screen';

export const Projects = () => {

  const projects1 = [
    {
      title: "Artist and Venue matching Web App",
      description: "The platform allows artists to post their profile and music, venues to post their space and key features, and event coordinators to create and schedule shows with ease. Whether planning an intimate performance or a large-scale concert, the web app streamlines the entire process, making it simple and hassle-free. ",
      imgUrl: projImg1,
      sourcelink: 'https://github.com/wendecoder/Portfolio_project/tree/master/flask_app',
    },
    {
      title: "Simple Trivia Web App",
      description: "The wep app allows users to browse a list of trivia questions, add new questions, and play trivia games using our collection of questions. Users can filter the questions by category and search for specific questions to find the perfect set for their game. With the platform, users can easily create fun and engaging trivia games for friends, family, or events. ",
      imgUrl: projImg2,
      sourcelink: 'https://github.com/wendecoder/Portfolio_project/tree/master/simpleTrivia',
    },
    {
      title: "Online Auctioning Web App",
      description: "The platform allows users to easily list items for auction, browse available items, and place bids on their favorite items. Users can filter the items by category, making it easier to find items that match their interests.",
      imgUrl: projImg3,
      sourcelink: 'https://github.com/wendecoder/Portfolio_project/tree/master/ShamoAuction',
    },
  ];
  const projects2 = [
    {
      title: "Coffee Shop Web App",
      description: "Coffee shop web app includes identity and access management using the Auth0 service. The app features an admin role, which enables users to create, edit, and delete drinks, and a user role, which allows users to view available drinks. The implementation of Auth0 ensures that user access is secure and that only authorized users can access sensitive functionality. ",
      imgUrl: projImg4,
      sourcelink: 'https://github.com/wendecoder/cd0039-Identity-and-Access-Management/tree/master/Project/03_coffee_shop_full_stack',
    },
    {
      title: "Server Deployment and Containerization",
      description: "My server deployment and containerization project involved containerizing a Flask application with Docker, building code pipelines on AWS, and deploying the containerized application onto an EKS Kubernetes cluster. ",
      imgUrl: projImg5,
      sourcelink: 'https://github.com/wendecoder/cd0157-Server-Deployment-and-Containerization',
    },
    {
      title: "Simple Shell",
      description: "The simple shell implementation includes additional functionalities beyond standard Linux commands. These functionalities include access (checks file access permissions), close (closes a file descriptor), execve (executes a program), _exit (terminates a process immediately), fflush (flushes a stream), isatty (checks if a file descriptor refers to a terminal), and signal (sets a signal handler).",
      imgUrl: projImg6,
      sourcelink: 'https://github.com/wendecoder/simple_shell',
    },
  ];

  return (
    <section className="project" id="projects">
      <Container>
        <Row>
          <Col size={12}>
            <TrackVisibility>
              {({ isVisible }) =>
              <div className={isVisible ? "animate__animated animate__fadeIn": ""}>
                <h2>Projects</h2>
                <p>I'm a skilled software engineer with extensive experience in programming and software development. Over the course of my career, I have participated in numerous projects in these fields, demonstrating my proficiency in a wide range of programming languages and tools. My projects have included everything from web application development to complex software systems design.
</p>
                <Tab.Container id="projects-tabs" defaultActiveKey="first">
                  <Nav variant="pills" className="nav-pills mb-5 justify-content-center align-items-center" id="pills-tab">
                    <Nav.Item>
                      <Nav.Link eventKey="first">Projects</Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                      <Nav.Link eventKey="second">More Projects</Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                      <Nav.Link eventKey="third">Watch Resume</Nav.Link>
                    </Nav.Item>
                  </Nav>
                  <Tab.Content id="slideInUp" className={isVisible ? "animate__animated animate__slideInUp" : ""}>
                    <Tab.Pane eventKey="first">
                      <Row>
                        {
                          projects1.map((project, index) => {
                            return (
                              <ProjectCard
                                key={index}
                                {...project}
                                />
                            )
                          })
                        }
                      </Row>
                    </Tab.Pane>
                    <Tab.Pane eventKey="second">
                      <Row>
                        {
                          projects2.map((project, index) => {
                            return (
                              <ProjectCard
                                key={index}
                                {...project}
                                />
                            )
                          })
                        }
                      </Row>
                    </Tab.Pane>
                    <Tab.Pane eventKey="third">
                     <DownloadButton/>
                    </Tab.Pane>
                  </Tab.Content>
                </Tab.Container>
              </div>}
            </TrackVisibility>
          </Col>
        </Row>
      </Container>
      <img className="background-image-right" src={colorSharp2}></img>
    </section>
  )
}
