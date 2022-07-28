import "./column.css";

/*
* Name: Leeden Raquel
* Author(s): Leeden Raquel
* Inputs:
*  children - the children in the element
* Description: organizes the children into a column
* Returns:
*  Column - a representation that organizes information into a column
*/
function Column({children}) {
    return (
        <div className="Column">
            {children}
        </div>
    );
}

export default Column;