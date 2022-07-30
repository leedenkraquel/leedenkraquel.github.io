import './navbar.css';
import NavbarItem from "./navbar-item";
import { useEffect, useState } from 'react';
import menuSmallInverted from "../images/menuSmallInverted.png"
import closeSmallInverted from "../images/closeSmallInverted.png"
import SideNavbarItem from './side-navbar-item';

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
    let [windowSize, setWindowSize] = useState({
        height: window.innerHeight,
        width: window.innerWidth,
    }); // the current window size 
    let [menuToggle, setMenuToggle] = useState(false); // the state of the menu
    let [menuClass, setMenuClass] = useState("Navbar-menu"); // the position of the menu button
    let [menuIcon, setMenuIcon] = useState(menuSmallInverted); // the icon of the menu button
    let [sideNavbarClass, setSideNavbarClass] = useState("SideNavbar"); // the position of the menu button

    useEffect(() => {
        window.addEventListener("resize", handleResize, false);
    }, []); // add a listener that runs the handle Resize function whenever the window is resized

    // when the window is resized update the window size variable
    function handleResize() {
        setWindowSize({
            width: window.innerWidth,
            height: window.innerHeight,
        });
    }

    // when the menu bottom is clicked toggle its state
    function menuOnClick() {
        setMenuToggle(!menuToggle);
        menuToggle ? setMenuClass("Navbar-menu-open") : setMenuClass("Navbar-menu");
        menuToggle ? setMenuIcon(closeSmallInverted) : setMenuIcon(menuSmallInverted);
        menuToggle ? setSideNavbarClass("SideNavbar-open") : setSideNavbarClass("SideNavbar");
    }

    // if the window is too thin to fit the entire navigation bar use a navigation menu
    if (windowSize.width < 700) {
        return (
            <div className="Navbar">
                <a className={menuClass} href="#" onClick={menuOnClick}>
                    <img src={menuIcon} alt="Menu Button" />
                </a>
                <div className={sideNavbarClass}>
                    <SideNavbarItem text="About" href="/" />
                    <SideNavbarItem text="Projects" href="/projects" />
                    <SideNavbarItem text="Essays" href="/essays" />
                    <SideNavbarItem text="Contact Me" href="/contact" />
                </div>
            </div>
        );
    } else { // otherwise use the navigatin bar
        return (
            <div className="Navbar">
                <NavbarItem text="About" href="/" />
                <NavbarItem text="Projects" href="/projects" />
                <NavbarItem text="Essays" href="/essays" />
                <NavbarItem text="Contact Me" href="/contact" />
            </div>
        );
    }
}

export default Navbar;