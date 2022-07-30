import "./navbar-item.css";

/*
* Name: NavbarItem
* Author(s): Leeden Raquel
* Inputs:
*  text - the text that is to be displayed in the item
* Description: the component item that represents the text 
*  items in the navigation bar
* Returns:
*  NavbarItem - the component that is rendered as the navigation bar item
*/
function NavbarItem(props) {
    return (
        <a className="Navbar-obj" href={props.href}>{props.text}</a>
    );
}

export default NavbarItem;