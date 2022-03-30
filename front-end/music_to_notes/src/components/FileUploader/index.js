import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Buffer} from 'buffer';
import ViewPdf from "../pdfViewer";

export const FileUploader = ({}) => {
    const [srcImage, setSrcImage] = useState("")

    const extract_extension = (name) => {
        return name.split(".").pop()
    }
    const extract_name = (name) => {
        return name.split(".")[0]
    }

    const renameFile = (originalFile, newName) => {
        var file_extension = extract_extension(originalFile.name)
        return new File([originalFile], newName + "." + file_extension, {
            type: originalFile.type,
            lastModified: originalFile.lastModified,
        });
    }
    const [origName, setOrigName] = useState(null);
    const [file, setFile] = useState(null);

    const randomString = () => {
        return Math.random().toString(36).substring(3, 9)
    }

    useEffect(() => {
        console.log("Orig name", origName)
    })

    const onInputChange = (e) => {
        // e.target.files[0].name = (Math.random() + 1).toString(36).substring(7)
        var file = renameFile(e.target.files[0], randomString())
        setFile(file)
        setOrigName(e.target.files[0].name)
    };

    const onSubmit = (e) => {
        e.preventDefault();
        const data = new FormData();
        data.append('file', file);
        data.append('type', 'png')
        axios.post('http://localhost:5000/api/audio', data, {
            responseType: "arraybuffer"
        })
            .then((response) => {
                console.log("Successfuly sent the file to server")
                console.log(response)
                let base64ImageString = Buffer.from(response.data, 'binary').toString('base64')
                let srcValue = "data:image/png;base64," + base64ImageString
                setSrcImage(srcValue)

                localStorage.setItem("filename", file.name)
                localStorage.setItem("origName", origName)
                localStorage.setItem("srcImage", srcImage)
            })
            .catch((e) => {
                console.log('Error', e)

            })

    };

    return (<div>
            <form method="post" action="#" id="#" onSubmit={onSubmit}>
                <label for="files" class="ui huge inverted button">Upload Song File </label>
                <input id="files" type="file"
                       onChange={onInputChange}
                       multiple=""
                       style={{visibility: 'hidden'}}
                />

                <button class="ui submit button">Submit</button>
            </form>

            {srcImage ? (
                <div>
                    <ViewPdf image={srcImage}/>
                </div>
            ) : <div></div>
            }
        </div>
    )
};