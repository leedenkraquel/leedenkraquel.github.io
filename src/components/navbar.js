import './navbar.css';
import NavbarItem from "./navbar-item";

/*
* Name: Navbar
* Author(s): Leeden Raquel
* Inputs:
*  None
* Description: the component at the top of every page that allows the user to navigate
*  through the site
* Returns:
*  Navbar - the component that is rendered as the navbar
*/
function Navbar() {
    return (
        <div className="Navbar">
            <NavbarItem text="About" />
            <NavbarItem text="Projects" />
            <NavbarItem text="Essays" />
            <NavbarItem text="Contact Me" />
        </div>
    );
}

export default Navbar;