import "./footer.css";
import Column from "../elements/column";
import VertRule from "../elements/vertrule";
import Sitemap from "./sitemap";

/*
* Name: Footer
* Author(s): Leeden Raquel
* Inputs:
*  None
* Description: the component at the bottom of every page that allows the user to navigate
*  through the site, other sites, and see a nice quote
* Returns:
*  Footer - the component that is rendered as the footer
*/
function Footer() {
    return (
        <div className="Footer">
            <Column>
                <Sitemap text="About" href="/" />
                <Sitemap text="Projects" href="/projects" />
                <Sitemap text="Essays" href="/essays" />
                <Sitemap text="Contact Me" href="/contact" />
            </Column>
            <VertRule />
            <Column>
                <p>icons</p>
            </Column>
            <VertRule />
            <Column>
                <p>Quote</p>
            </Column>
        </div>
    );
}

export default Footer;