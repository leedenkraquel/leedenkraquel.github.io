import "./side-navbar-item.css";

/*
* Name: SideNavbarItem
* Author(s): Leeden Raquel
* Inputs:
*  text - the text that is to be displayed in the item
* Description: the component item that represents the text 
*  items in the side navigation bar
* Returns:
*  SideNavbarItem - the component that is rendered as the side navigation bar item
*/
function SideNavbarItem(props) {
    return (
        <a className="SideNavbar-obj" href={props.href}>{props.text}</a>
    );
}

export default SideNavbarItem;