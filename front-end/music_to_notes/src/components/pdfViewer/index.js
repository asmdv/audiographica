import React from "react";
import './pdfViewer.css'
import axios from "axios";
import FileSaver from 'file-saver';


const ViewPdf = ({image}) => {

    const extract_name = (name) => {
        return name.split(".")[0]
    }

    const onSubmit = (e) => {
        e.preventDefault();

        var filename = localStorage.getItem("filename")
        var origName = localStorage.getItem("origName")
        console.log("Filename is ", filename)
        return axios.post('http://localhost:5000/api/pdf', {filename: filename}, {
            responseType: 'blob'
        })
            .then((response) => {
                console.log("Successfuly sent the file to server")
                var blob = new Blob([response.data], {type: "application/pdf"})
                FileSaver.saveAs(blob, extract_name(origName) + ".pdf")
            })
            .catch((e) => {
                console.log('Error', e)

            })


    };

    return (
        <div id="display">
            <a class="ui inverted green button" id="download" href={image} download onClick={onSubmit}><i
                class="download icon"></i>Click to download </a>
            <button class="ui inverted red button"> Clear</button>
            <img src={image} alt="Sheet Music failed to upload"/>
        </div>);
};

export default ViewPdf;