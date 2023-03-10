import meter1 from "../assets/img/meter1.svg";
import meter2 from "../assets/img/meter2.svg";
import meter3 from "../assets/img/meter3.svg";
import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';
import arrow1 from "../assets/img/arrow1.svg";
import arrow2 from "../assets/img/arrow2.svg";
import colorSharp from "../assets/img/color-sharp.png"

export const Skills = () => {
  const responsive = {
    superLargeDesktop: {
      // the naming can be any, depends on you.
      breakpoint: { max: 4000, min: 3000 },
      items: 5
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 3
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 2
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1
    }
  };

  return (
    <section className="skill" id="skills">
        <div className="container">
            <div className="row">
                <div className="col-12">
                    <div className="skill-bx wow zoomIn">
                        <h2>Skills</h2>
                        <p>As a full stack developer, I possess a wide range of skills that allow me to work effectively across the entire technology stack. On the front end, I have expertise in HTML, CSS, React, and Bootstrap, which enables me to create beautiful and responsive user interfaces that deliver a seamless user experience. On the backend, I have proficiency in Flask, Node.js, Python, MySQL, and PostgreSQL, allowing me to build robust, scalable, and secure web applications that can handle high levels of traffic and complex data interactions.</p>
                        <br />
                        <p>In addition, I have extensive knowledge of system DevOps and Git version control, which helps me to streamline the development process and maintain well-organized code that can be easily managed and maintained. Finally, my proficiency in server deployment on cloud services like AWS ensures that the applications I build are delivered to a global audience with minimal downtime and maximum reliability.</p>
                        <br />
                        <p>Overall, my skills as a full stack developer make me a valuable asset to any software development team, and I am confident in my ability to build high-quality web applications that meet the needs of businesses and users alike.</p>
                        <Carousel responsive={responsive} infinite={true} className="owl-carousel owl-theme skill-slider">
                            <div className="item">
                                <img src={meter1} alt="Image" />
                                <h5>Frontend Web Development</h5>
                            </div>
                            <div className="item">
                                <img src={meter1} alt="Image" />
                                <h5>Backend Web Development</h5>
                            </div>
                            <div className="item">
                                <img src={meter3} alt="Image" />
                                <h5>Git Version Control</h5>
                            </div>
                            <div className="item">
                                <img src={meter3} alt="Image" />
                                <h5>Server Deployment</h5>
                            </div>
                        </Carousel>
                    </div>
                </div>
            </div>
        </div>
        <img className="background-image-left" src={colorSharp} alt="Image" />
    </section>
  )
}
