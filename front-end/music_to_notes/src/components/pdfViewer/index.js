import React from "react";
import { useState } from "react";
import image from './Notes.png'
import './pdfViewer.css'
  

const ViewPdf = ()=>{

    return ( 
    <div id="display">
        <a class="ui inverted green button" id="download" href={image} download><i class="download icon"></i>Click to download </a>
        <button class="ui inverted red button" > Clear </button>
       <img src={image} alt="Sheet Music failed to upload" />
    </div>);
}; 

export default ViewPdf;