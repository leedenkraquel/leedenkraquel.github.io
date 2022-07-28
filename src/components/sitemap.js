import "./sitemap.css";

/*
* Name: Sitemap
* Author(s): Leeden Raquel
* Inputs:
*  children - the children in the element
* Description: organizes the elements into a sitemap
* Returns:
*  Sitemap - the sitemap element to be rendered
*/
function Sitemap({children}) {
    return (
        <a className="Sitemap">{children}</a>
    );
}

export default Sitemap;