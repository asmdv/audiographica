import React, {useEffect} from "react";
import { useState } from "react";
import image from './Notes.png'
import './pdfViewer.css'
import axios from "axios";
import download from "downloadjs";
  

const ViewPdf = ({ image })=>{

    const extract_name = (name) => {
        return name.split(".")[0]
    }

    const onSubmit = (e) =>{
        e.preventDefault();

        var filename = localStorage.getItem("filename")
        var origName = localStorage.getItem("origName")
        axios.post('http://localhost:5000/api/pdf', {filename: filename})
            .then((response)=>{
                console.log("Successfuly sent the file to server")
                console.log("Response", response)
                download(response.data, extract_name(origName) + ".pdf", response.headers['content-type'])
            })
            .catch((e)=>{
                console.log('Error',e)

            })


    };

    return ( 
    <div id="display">
        <a class="ui inverted green button" id="download" href={image} download onClick={onSubmit}><i class="download icon"></i>Click to download </a>
        <button class="ui inverted red button" > Clear </button>
        <img src={image} alt="Sheet Music failed to upload" />
    </div>);
}; 

export default ViewPdf;