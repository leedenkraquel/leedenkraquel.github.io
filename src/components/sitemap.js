import "./sitemap.css";

/*
* Name: Sitemap
* Author(s): Leeden Raquel
* Inputs:
*  props - the props in the element
* Description: organizes the elements into a sitemap
* Returns:
*  Sitemap - the sitemap element to be rendered
*/
function Sitemap(props) {
    return (
        <a className="Sitemap" href={props.href}>{props.text}</a>
    );
}

export default Sitemap;