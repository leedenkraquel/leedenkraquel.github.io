import './App.css';
import Footer from './components/footer';
import Body from './components/body';
import Navbar from './components/navbar';
import { BrowserRouter } from 'react-router-dom';

/*
* Name: App
* Author(s): Leeden Raquel
* Inputs: 
*  None
* Description: The top level app of the site
* Returns:
*  App - the react element that is rendered as the app
*/
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Navbar />
        <Body />
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
