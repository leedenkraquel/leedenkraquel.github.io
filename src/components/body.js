import "./body.css";
import { Routes, Route } from 'react-router-dom';

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
                <Route exact path="/" element={ <p>Body</p> } />
                <Route path="*" element={ <p>404 page</p> } />
            </Routes>
        </div>
    );
}

export default Body;