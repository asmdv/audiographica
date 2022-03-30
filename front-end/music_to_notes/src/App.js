import Home from './HomePage.js'
import { FileUploader } from './components/FileUploader/index.js';
import  ViewPdf  from './components/pdfViewer/index.js';

import './App.css'
function App() {
  return (
    <div >
      <Home/>
      <FileUploader/>
      {/*<ViewPdf/>*/}
    </div>
   
  );
}

export default App;
