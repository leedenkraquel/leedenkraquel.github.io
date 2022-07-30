import "./body.css";
import { Routes, Route } from 'react-router-dom';
import About from "../pages/about";
import Projects from "../pages/projects";
import Essays from "../pages/essays";
import Contact from "../pages/contact";

/*
* Name: Body
* Inputs:
*  None
* Description: represents the body of the site
* Returns:
*  Body - the body element to be rendered
*/
function Body() {
    return (
        <div className="Site-Body">
            <Routes>
                <Route exact path="/" element={ <About /> } />
                <Route exact path="/projects" element={ <Projects /> } />
                <Route exact path="/essays" element={ <Essays /> } />
                <Route exact path="/contact" element={ <Contact /> } />
                <Route path="*" element={ <p>404 page</p> } />
            </Routes>
        </div>
    );
}

export default Body;