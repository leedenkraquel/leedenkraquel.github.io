import "./navbar-item.css";
import { useNavigate } from "react-router-dom";

/*
* Name: NavbarItem
* Author(s): Leeden Raquel
* Inputs:
*  text - the text that is to be displayed in the item
* Description: the component item that represents the text 
*  items in the navbar
* Returns:
*  NavbarItem - the component that is rendered as the navbar item
*/
function NavbarItem(props) {
    let navigate = useNavigate(); // hook used to change the route of the web app

    function onClick() {
        navigate("/test");
    }

    return (
        <a className="Navbar-obj" href="" onClick={onClick}>{props.text}</a>
    );
}

export default NavbarItem;